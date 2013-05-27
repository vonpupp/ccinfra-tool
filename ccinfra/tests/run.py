#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import sys
from ccinfra.model.filebuilder import FileBuilder
import os
#import pudb


class FileBuilderTestCase(unittest.TestCase):
    fb = None

    def setUp(self):
        self.fb = FileBuilder()
        self.fb.set_in_path('../../conf/srv/')
        #self.fb.set_in_path('../../conf/srv/etc')
        self.fb.set_out_path('out2/')
        
    def test_000paths(self):
        self.fb.set_file_in('/etc/dhcpd.conf')
#         self.fb.get_path_and_full_conf()
#         self.fb.get_io_confs()
#         self.fb.get_io_paths()

    def test_dhcpd_file_exists(self):
        exists = os.path.exists(LOCAL_INSTALL_DIR)
        assertTrue(exists)

    def test_dhcpd_file_line_count(self):
        filename = sys._getframe().f_code.co_name + '.csv'
        d = self.rb.model.uniquerfi
        tagstr = 'RFI'
        self.tag_check(filename, d, tagstr)


def fast_tests_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(FileBuilderTestCase))
    return suite

def slow_test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(FileBuilderTestCase))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(fast_tests_suite())
