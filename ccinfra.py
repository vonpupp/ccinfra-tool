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
__version__ = '0.1'
__author__ = 'Albert De La Fuente'
__copyright__ = '2013 Congregacao Crista no Brasil / Albert De La Fuente'

'''
    A tool for automatic lconfiguration for servers and desktops

    Command Line Usage:
        ccinfra.py {<option> <arguments>}

    Options:
        -h, --help
        srv <service>
        cli <service>

    Arguments:

    Examples:
'''

import sys
import argparse
from subprocess import call
from ccinfra.model.filebuilder import FileBuilder
from ccinfra.model.confiterator import ConfIterator
from ccinfra.model.model import ServerSetup


def main(argv):
    # Parse arguments
    #parser = argparse.ArgumentParser()
    #parser.add_argument('--verbose', help='increase output verbosity',
    #                    action='store_true')
    #parser.add_argument('srv', nargs='?', help='server',
    #                    action='store_true')
    #args = parser.parse_args()

    # Clone the config repository
#    call(['sh', 'clone.sh'])

    # Create structures
    fb = FileBuilder()
    iterator = ConfIterator()

    # Initialize structures
    fb.set_out_path('out/etc/')
    iterator.set_input_path('conf/srv/')

    # Do stuff
    srv = ServerSetup()
    srv.set_in_path('conf/')
    srv.set_out_path('out/')
    srv.isc_dhcpd_setup()
    srv.named_keys_setup()
    srv.named_setup()
#    fb.build_file('conf/srv/etc/named.conf')
#    for filename in iterator.files():
#        fb.build_file(filename)
#        print filename

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
