#!/usr/bin/python

from string import Template

# class MyTemplate(string.Template):
#     delimiter = '%'
#     idpattern = '[a-z]+_[a-z]+'

params = { 'uuid':'br210008',
#           'domain':'br210008.congregacao.org.br',
           'ccdomain':'congregacao.org.br',
           'server':'10.0.0.1',
#           'nameserver1':'10.0.0.1',
           'nameserver2':'208.67.220.220',
#           'gw':'10.0.0.1',
           'rndcfile':'/etc/named.d/dns.key',
           'rndckey':'dhcp_updates',
           'subnet':'10.0.0.0',
           'netmask':'255.255.252.0',
           'dhcpdstart':'10.0.0.31',
           'dhcpdend':'10.0.3.240',
#           'dnsforwardzone':'br210008.congregacao.org.br.',
           'dnsreversezone':'0.0.10.in-addr.arpa',
         }

fin = open('conf/dhcpd.conf')
fout = open('out/dhcpd.conf', 'w')
for line in fin:
    out_line = line
    s = Template(line)
#    if '$fqdn' in line:
    try:
        out_line = s.substitute(params)
    except KeyError, err:
        print 'ERROR: ' + str(err) + ' variable is missing'
    fout.write(out_line)
