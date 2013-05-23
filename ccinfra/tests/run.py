#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import random
import sys
import inspect
import codecs
import csv
from ccinfra.model.filebuilder import FileBuilder


rb = None

class FileBuilderTestCase(unittest.TestCase):
    fb = None

    def setUp(self):
        self.fb = FileBuilder()
        #self.seq = range(10)

    #def uckeymeasure(self, key):
    #    #result = self.rb.model.fp.fundict[key][1:] #and key
    #    result = key #and key
    #    return result

    def tag_check(self, filename, d, tagstr):
        """
        Verifica se foi pulado algum tagstr no dict d e guarda os resultados
        no arquivo filename
        """
        fh = codecs.open(filename, encoding='utf-8', mode='w') # open(filename, 'r')
        csvhdlr = csv.writer(fh, delimiter='\t')#, quotechar='"')#, quoting=csv.QUOTE_MINIMAL)

        itemscount = len(d)
        maxid = max(d)
        if maxid.startswith(tagstr):
            maxid = maxid[len(tagstr):]
        #item = max(d, key=self.uckeymeasure)
        #maxid = max(self.uckeymeasure(k) for k in d.keys())
        csvhdlr.writerow(["ID", "Tipo", "Pulados"])
        for number in range(1, int(maxid) + 1):
            item = tagstr + '%03d' % number
            reqid = item
            reqname = ''
            reqtype = tagstr
            reqbody = ''
            try:
                self.assertIn(item, d)
                status = 'ok'
            except:
                status = 'FAILED'
                if self.rb.stricttests:
                    raise
            row = [reqid, reqtype, status]
            csvhdlr.writerow(row)

    def test_parser_0101_missing_uc_objects(self):
        """
        Verifica se foi pulado algum numero de UC na sequencia
        """
        filename = sys._getframe().f_code.co_name + '.csv'
        d = self.rb.model.fp.fundict
        tagstr = 'UC'
        self.tag_check(filename, d, tagstr)

    def test_parser_0102_missing_rfi_objects(self):
        """
        Verifica se foi pulado algum numero de RFI na sequencia
        """
        filename = sys._getframe().f_code.co_name + '.csv'
        d = self.rb.model.uniquerfi
        tagstr = 'RFI'
        self.tag_check(filename, d, tagstr)


def fast_tests_suite():
    #args = sys.argv[1:]
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestMissingObjects))
    suite.addTest(unittest.makeSuite(TestOrphanObjects))
    suite.addTest(unittest.makeSuite(TestOrphanUCRel))
    suite.addTest(unittest.makeSuite(TestFuzzyStrMatch))
    return suite

def slow_test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestEAIntegrity))
    return suite

if __name__ == '__main__':
#    unittest.main(verbosity=2)


    suiteFew = unittest.TestSuite()
    #suiteFew.addTest(TestMissingObjects("test_01_UC_missing"))
    #suiteFew.addTest(TestMissingObjects("test_shuffle"))
    #unittest.TextTestRunner(verbosity=2).run(suiteFew)
    unittest.TextTestRunner(verbosity=2).run(fast_tests_suite())

#suite1 = unittest.TestSuite(MyTestCase1(), MyTestCase2())
#suite2 = unittest.TestSuite()
#suite2.addTest(MyOtherTestCase())
#
#big_suite = unittest.TestSuite(suite1)
#big_suite.addTest(suite2)
