#!/usr/bin/python

from string import Template
import json
from pprint import pprint

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


def FileBuilder(input_conf):
    try:

        input_filename = split(input_conf, "/")[:-1]
        import pdb; pdb.trace()
        output_filename = 'out/' + split(input_conf, "/")
        fin = open(input_conf)
        fout = open(output_filename, 'w')

        f = open('conf/conf.json')

        jdata = json.load(f)
        pprint(jdata)
        f.close()

        js = json.dumps(jdata, sort_keys=True,
                        indent=4, separators=(',', ' : '))
        print js
        for line in fin:
            out_line = line
            s = Template(line)
        #    if '$fqdn' in line:
            try:
                out_line = s.substitute(jdata['vars'])
            except KeyError, err:
                print 'ERROR: ' + str(err) + ' variable is missing'
            fout.write(out_line)
    except Exception, e:
        raise e
