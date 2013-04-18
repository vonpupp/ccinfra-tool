#!/usr/bin/python

from string import Template

# class MyTemplate(string.Template):
#     delimiter = '%'
#     idpattern = '[a-z]+_[a-z]+'

params = { 'fqdn':'br210008.congregacao.org.br',
           'nameserver1':'127.0.0.1',
           'nameserver2':'8.8.8.8',
           'gw':'8.8.8.8',
           'rndcfile':'8.8.8.8',
           'rndckey':'8.8.8.8',
           'subnet':'8.8.8.8',
           'mask':'8.8.8.8',
           'dnsforwardzone':'8.8.8.8',
           'dnsreversezone':'8.8.8.8',
           'dhcpdstart':'8.8.8.8',
           'dhcpdend':'8.8.8.8',
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
