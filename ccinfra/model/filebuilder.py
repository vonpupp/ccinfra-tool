#!/usr/bin/python

from string import Template
import json
from pprint import pprint
import os

# class MyTemplate(string.Template):
#     delimiter = '%'
#     idpattern = '[a-z]+_[a-z]+'

# params = { 'uuid':'br210008',
# #           'domain':'br210008.congregacao.org.br',
#            'ccdomain':'congregacao.org.br',
#            'server':'10.0.0.1',
# #           'nameserver1':'10.0.0.1',
#            'nameserver2':'208.67.220.220',
# #           'gw':'10.0.0.1',
#            'rndcfile':'/etc/named.d/dns.key',
#            'rndckey':'dhcp_updates',
#            'subnet':'10.0.0.0',
#            'netmask':'255.255.252.0',
#            'dhcpdstart':'10.0.0.31',
#            'dhcpdend':'10.0.3.240',
# #           'dnsforwardzone':'br210008.congregacao.org.br.',
#            'dnsreversezone':'0.0.10.in-addr.arpa',
#          }
OUTDIR = 'out/'

def FileBuilder(input_confpath):
    try:
        # I assume that conf/srv (two dirs) are always prepended to the path
        relative_etc_filename = input_confpath.split('etc/')[1]
        output_confpath = OUTDIR + 'etc/' + relative_etc_filename
        
        filename = output_confpath.split('/')[-1]
        directory = output_confpath.replace(filename, '')
        
        fin = open(input_confpath)
        try:
            fout = open(output_confpath, 'w')
        except:
            os.makedirs(directory)

        #vars_file = filename.split('.')[0]
        fvars = open(input_confpath + '.vars')

        vars_data = json.load(fvars)
        fvars.close()
        #pprint(vars_data)
        
        js = json.dumps(vars_data, sort_keys=True,
                        indent=4, separators=(',', ' : '))
        print js
        try:
            for line in fin:
                try:
                    out_line = line
                    s = Template(line)
                    out_line = s.substitute(vars_data['vars'])
                    fout.write(out_line)
                except KeyError, err:
                    print 'ERROR: ' + str(err) + ' variable is missing'
        finally:
            fout.close()
            fin.close()
        return output_confpath
    except Exception, e:
        raise e
