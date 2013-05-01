#!/usr/bin/python

from string import Template
import json
from pprint import pprint
import os

OUTDIR = 'out/'

# class MyTemplate(string.Template):
#     delimiter = '%'
#     idpattern = '[a-z]+_[a-z]+'

def FileBuilder(input_conf):
    try:
        # I assume that conf/srv (two dirs) are always prepended to the path
        conf_path, conf_file = get_path_and_full_conf(input_conf)
        input_conf, output_conf = get_io_confs(input_conf)
        input_path, output_path = get_io_paths(input_conf)
        
        fin = open(input_conf)
        fout = open_or_create_dir(output_conf)

        vars_data = load_vars(input_conf)
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
        return output_conf
    except Exception, e:
        raise e
    
def open_or_create_dir(output_conf):
    input_path, output_path = get_io_paths(output_conf)
    try:
        result = open(output_conf, 'w')
    except:
        os.makedirs(output_path)
    return result

def get_path_and_full_conf(input_conf):
    conf_file = input_conf.split('/')[-1]
    conf_path = input_conf.rsplit('/', 1)[0]
    return conf_path, conf_file

def get_io_confs(input_conf):
    relative_etc_conf = input_conf.split('etc/')[1]
    output_conf = OUTDIR + 'etc/' + relative_etc_conf

    return input_conf, output_conf

def get_io_paths(input_conf):
    _, conf_file = get_path_and_full_conf(input_conf)
    input_conf, output_conf = get_io_confs(input_conf)
    input_path = input_conf.replace(conf_file, '')
    output_path = output_conf.replace(conf_file, '')
    
    return input_path, output_path

def load_vars_file(input_conf):
    try:
        fvars = open(input_conf + '.vars')
        vars_data = json.load(fvars)
        fvars.close()
        return vars_data
    except:
        return {'vars':{}}
        
def load_vars(input_conf):
    try:
        _, conf_file = get_path_and_full_conf(input_conf)
        input_path, _ = get_io_paths(input_conf)
        vars_global = {}
        vars_common = {}
        vars_conf = {}
        # First load the globals
        vars_global = load_vars_file(input_path + 'ccinfra.global')
        # Then the commons
        vars_common = load_vars_file(input_path + 'ccinfra.common')
        # Finally the local conf (overrides will be down-top)
        vars_conf = load_vars_file(input_conf)
    finally:
        vars_data = {'vars': dict(vars_global['vars'].items() +
                                  vars_common['vars'].items() +
                                  vars_conf['vars'].items())
                    }
        return vars_data