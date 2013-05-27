#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase, TestSuite, makeSuite, TextTestRunner
import sys
from ccinfra.model.filebuilder import FileBuilder
import os
#import pudb

INPATH = '../../conf/srv/'
OUTPATH = 'out2/'

class FileBuilderTestCase(TestCase):
    fb = None

    def setUp(self):
        self.fb = FileBuilder()
        self.fb.set_in_path(INPATH)
        #self.fb.set_in_path('../../conf/srv/etc')
        self.fb.set_out_path(OUTPATH)
        
    def test_000paths(self):
        self.fb.set_file_in('/etc/dhcpd.conf')
#         self.fb.get_path_and_full_conf()
#         self.fb.get_io_confs()
#         self.fb.get_io_paths()

    def test_dhcpd_file_exists(self):
        exists = os.path.exists(OUTPATH + 'dhcpd.conf')
        self.assertTrue(exists)

    def test_dhcpd_file_line_count(self):
        pass


def fast_tests_suite():
    suite = TestSuite()
    suite.addTest(makeSuite(FileBuilderTestCase))
    return suite

def slow_test_suite():
    suite = TestSuite()
    suite.addTest(makeSuite(FileBuilderTestCase))
    return suite

if __name__ == '__main__':
    TextTestRunner(verbosity=2).run(fast_tests_suite())
