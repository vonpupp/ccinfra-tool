from __future__ import print_function

import sys
py3 = (sys.version_info >= (3,0))

# some test helpers

_target = None
_tempfiles = []
_logfile = None

def success():
    import sys
    success.count += 1
    if _logfile:
        print(sys.argv[0], success.count, failure.count, file=_logfile)

def failure(msg=None, frame=None):
    import sys, linecache
    failure.count += 1
    if _target:
        if frame is None:
            frame = sys._getframe()
            while frame.f_globals.get("__name__") != _target.__name__:
                frame = frame.f_back
        location = (frame.f_code.co_filename, frame.f_lineno)
        prefix = "%s:%d: " % location
        line = linecache.getline(*location)
        print(prefix + line.strip() + " failed:")
    if msg:
        print("- " + msg)
    if _logfile:
        print(sys.argv[0], success.count, failure.count, file=_logfile)

success.count = failure.count = 0

# predicates

def assert_true(v, msg=None):
    if v:
        success()
    else:
        failure(msg or "got %r, expected true value" % v)

def assert_false(v, msg=None):
    if v:
        failure(msg or "got %r, expected false value" % v)
    else:
        success()

def assert_equal(a, b, msg=None):
    if a == b:
        success()
    else:
        failure(msg or "got %r, expected %r" % (a, b))

def assert_match(v, pattern, msg=None):
    import re
    if re.match(pattern, v):
        success()
    else:
        failure(msg or "got %r, doesn't match pattern %r" % (v, pattern))

def assert_exception(exc_class, func):
    import sys, traceback
    try:
        func()
    except exc_class:
        success()
    except:
        failure("expected %r exception, got %r" % (
                exc_class.__name__, sys.exc_info()[0].__name__))
        traceback.print_exc()
    else:
        failure("expected %r exception, got no exception" % exc_class.__name__)

def assert_no_exception(func):
    import sys, traceback
    try:
        func()
    except:
        failure("expected no exception, got %r" % sys.exc_info()[0].__name__)
        traceback.print_exc()
    else:
        success()

def assert_warning(warn_class, func):
    # note: this assert calls func three times!
    import warnings
    def warn_error(message, category, **options):
        raise category(message)
    def warn_ignore(message, category, **options):
        pass
    warn = warnings.warn
    result = None
    try:
        warnings.warn = warn_ignore
        assert_no_exception(func)
        result = func()
        warnings.warn = warn_error
        assert_exception(warn_class, func)
    finally:
        warnings.warn = warn # restore
    return result

# helpers

from io import BytesIO

def fromstring(data):
    from PIL import Image
    return Image.open(BytesIO(data))

def tostring(im, format, **options):
    out = BytesIO()
    im.save(out, format, **options)
    return out.getvalue()

def tempfile(template, *extra):
    import os, os.path, sys, tempfile
    files = []
    root = os.path.join(tempfile.gettempdir(), 'ccinfra-tool-tests')
    try:
        os.mkdir(root)
    except OSError:
        pass
    for temp in (template,) + extra:
        assert temp[:5] in ("temp.", "temp_")
        name = os.path.basename(sys.argv[0])
        name = temp[:4] + os.path.splitext(name)[0][4:]
        name = name + "_%d" % len(_tempfiles) + temp[4:]
        name = os.path.join(root, name)
        files.append(name)
    _tempfiles.extend(files)
    return files[0]

# test runner

def run():
    global _target, _tests, run
    import sys, traceback
    _target = sys.modules["__main__"]
    run = None # no need to run twice
    tests = []
    for name, value in list(vars(_target).items()):
        if name[:5] == "test_" and type(value) is type(success):
            tests.append((value.__code__.co_firstlineno, name, value))
    tests.sort() # sort by line
    for lineno, name, func in tests:
        try:
            _tests = []
            func()
            for func, args in _tests:
                func(*args)
        except:
            t, v, tb = sys.exc_info()
            tb = tb.tb_next
            if tb:
                failure(frame=tb.tb_frame)
                traceback.print_exception(t, v, tb)
            else:
                print("%s:%d: cannot call test function: %s" % (
                    sys.argv[0], lineno, v))
                failure.count += 1

def yield_test(function, *args):
    # collect delayed/generated tests
    _tests.append((function, args))

def skip(msg=None):
    import os
    print("skip")
    os._exit(0) # don't run exit handlers

def _setup():
    global _logfile
    def report():
        if run:
            run()
        if success.count and not failure.count:
            print("ok")
            # only clean out tempfiles if test passed
            import os, os.path, tempfile
            for file in _tempfiles:
                try:
                    os.remove(file)
                except OSError:
                    pass # report?
            temp_root = os.path.join(tempfile.gettempdir(), 'ccinfra-tool-tests')
            try:
                os.rmdir(temp_root)
            except OSError:
                pass

        if "--coverage" in sys.argv:
            import coverage
            coverage.stop()
            # The coverage module messes up when used from inside an
            # atexit handler.  Do an explicit save to make sure that
            # we actually flush the coverage cache.
            coverage.the_coverage.save()
    import atexit, sys
    atexit.register(report)
    if "--coverage" in sys.argv:
        import coverage
        coverage.start()
    if "--log" in sys.argv:
        _logfile = open("test.log", "a")


_setup()
