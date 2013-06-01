
import unittest
import tests.run as ccit

#suiteFew = unittest.TestSuite()
unittest.TextTestRunner(verbosity=2).run(ccit.tests_suite())
