#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#   Project:		CCInfra
#   Component Name:	Main
#   Language:           Python2
#
#   License:            GPLv2
#
#   Author:             Albert De La Fuente (www.albertdelafuente.com)
#   E-Mail:             albert.delafuente [at] congregacao _dot_ org *dot* br
#
#   Description:	A tool for automatic configuration for
#                       servers and desktops
#
#   Dependencies:
#
__version__ = "0.1"
__author__ = "Albert De La Fuente"
__copyright__ = "2013 Congregacao Crista no Brasil / Albert De La Fuente"

"""
    A tool for automatic lconfiguration for servers and desktops

    Command Line Usage:
        ccinfra.py {<option> <arguments>}

    Options:
        -h, --help
        srv <service>
        cli <service>

    Arguments:

    Examples:
"""


import getopt
import sys

def main(argv):

    try:
        optlist, args = getopt.getopt(argv, 'hv:p:aingo:t', [
            'help', 'verbose',
            'parse'
            'export-all', 'export-rfi', 'export-rfn', 'in-objects',
            'parse-v7', 'parse-v8', 'run-tests', 'strict-tests'])
    except getopt.GetoptError, msg:
        sys.stderr.write("ccinfra: error: %s" % msg)
        sys.stderr.write("See 'ccinfra --help'.\n")
        return 1

    # Create structures
    rb = ReqBox()
    rb.parserverion = 7

    # Parse options
    for opt, optarg in optlist:
        if opt in ('-h', '--help'):
            sys.stdout.write(__doc__)
            return 0
        elif opt in ('-v', '--verbose'):
            log_setverbosity(int(optarg))
            pass
        elif opt in ('-p', '--parse'):
            if optarg.lower() == 'v7':
                rb.parserverion = 7
            elif optarg.lower() == 'v8':
                rb.parserverion = 8
        elif opt in ('-o', '--in-objects'):
            rb.inputdir = optarg

        # Map options to structures
        rb.inputfile = args[0]
        rb.parseall = rb.parseall or opt in ('-a', '--export-all')
        rb.parsefun = rb.parseall or rb.parsefun or opt in ('-f', '--export-fun')
        rb.parserfi = rb.parseall or rb.parserfi or opt in ('-i', '--export-rfi')
        rb.parserfn = rb.parseall or rb.parserfn or opt in ('-r', '--export-rfn')
        rb.parsernf = rb.parseall or rb.parsernf or opt in ('-n', '--export-rnf')
        rb.parsergn = rb.parseall or rb.parsergn or opt in ('-g', '--export-rgn')
        rb.parseext = rb.parseall or rb.parseext or opt in ('-e', '--export-ext')
        rb.parseinc = rb.parseall or rb.parseinc or opt in ('-n', '--export-inc')
        rb.parseimp = rb.parseall or rb.parseimp or opt in ('-m', '--export-imp')
        rb.runtests = rb.runtests or opt in ('-t', '--run-tests')
        rb.stricttests = rb.stricttests or opt == '--strict-tests'

    # Initialize structures
    rb.initparser()
    rb.model.parsefile(rb.inputfile)

    # Do stuff
    if rb.parsefun and rb.parserverion == 7:
        rb.parsefunobjects("out-fun-objects.csv")
        rb.parsefunrfilinks("out-fun-rfi-links.csv")
        rb.parsefunrfnlinks("out-fun-rfn-links.csv")
        rb.parsefunrgnlinks("out-fun-rgn-links.csv")
        rb.parsefunrnflinks("out-fun-rnf-links.csv")

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
