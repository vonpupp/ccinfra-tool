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
import argparse


def main(argv):
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--verbose", help="increase output verbosity",
                        action="store_true")
    args = parser.parse_args()

    # Create structures
    rb = ReqBox()
    rb.parserverion = 7

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
