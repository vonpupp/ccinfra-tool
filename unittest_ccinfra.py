
import unittest
import ccinfra.tests.run as ccit

#suiteFew = unittest.TestSuite()
unittest.TextTestRunner(verbosity=2).run(ccit.fast_tests_suite())
