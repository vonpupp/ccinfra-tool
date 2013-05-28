#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase, TestSuite, makeSuite, TextTestRunner
import sys
from ccinfra.model.filebuilder import FileBuilder
import os
import shutil
#import pudb

INPATH = 'conf/srv/'
OUTPATH = 'tests-out/'

class FileBuilderTestCase(TestCase):
    fb = None

    def setUp(self):
        self.fb = FileBuilder()
        self.fb.set_in_path(INPATH)
        #self.fb.set_in_path('../../conf/srv/etc')
        self.fb.set_out_path(OUTPATH)
       
    def remove_dir(self, directory):
        if os.path.exists(directory):
            shutil.rmtree(directory)

    ###

    def test_000paths(self):
        self.fb.set_file_in('/etc/dhcpd.conf')
        self.assertTrue(len(self.fb.full_conf) ==
                        len(self.fb.conf_path) + len(self.fb.conf_file) + 1)
        self.assertTrue(self.fb.input_conf in self.fb.full_conf)
        self.assertTrue(self.fb.conf_file in self.fb.full_conf)
        self.assertTrue(self.fb.conf_file in self.fb.output_conf)

    def test_dhcpd_file_exists(self):
        in_conf = '/etc/dhcpd.conf'
        out_conf = 'dhcpd.conf'
        
        self.remove_dir(OUTPATH)
        self.assertFalse(os.path.exists(OUTPATH))
        
        self.fb.build_file(in_conf)
        
        self.assertTrue(os.path.exists(OUTPATH))

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
