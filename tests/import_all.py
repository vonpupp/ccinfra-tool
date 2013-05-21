import sys
sys.path.insert(0, ".")

import glob, os
import traceback

for file in glob.glob("ccinfra/*.py"):
    module = os.path.basename(file)[:-3]
    try:
        exec("from ccinfra import " + module)
    except (ImportError, SyntaxError):
        print("===", "failed to import", module)
        traceback.print_exc()
