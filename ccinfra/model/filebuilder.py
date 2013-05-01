#!/usr/bin/python

from string import Template
import json
from pprint import pprint
import os

OUTDIR = 'out/'

# class MyTemplate(string.Template):
#     delimiter = '%'
#     idpattern = '[a-z]+_[a-z]+'


class FileBuilder():
    def FileBuilder():
        self.conf_file = ''
        self.conf_path = ''
        self.input_path = ''
        self.output_path = ''
        
    def set_out_path(self, output_path):
        self.output_path = output_path

    def open_or_create_dir(self):
        self.input_path, self.output_path = self.get_io_paths()
        try:
            result = open(self.output_conf, 'w')
        except:
            os.makedirs(self.output_path)
        return result
    
    def get_path_and_full_conf(self):
        self.conf_file = self.input_conf.split('/')[-1]
        self.conf_path = self.input_conf.rsplit('/', 1)[0]
        
        return self.conf_path, self.conf_file
    
    def get_io_confs(self):
        self.relative_etc_conf = self.input_conf.split('etc/')[1]
        self.output_conf = OUTDIR + 'etc/' + self.relative_etc_conf
    
        return self.input_conf, self.output_conf
    
    def get_io_paths(self):
        self.get_path_and_full_conf()
        self.get_io_confs()
        self.input_path = self.input_conf.replace(self.conf_file, '')
        self.output_path = self.output_conf.replace(self.conf_file, '')
        
        return self.input_path, self.output_path
    
    def load_vars_file(self, input_conf):
        try:
            fvars = open(input_conf + '.vars')
            vars_data = json.load(fvars)
            fvars.close()
            return vars_data
        except:
            return {'vars':{}}
            
    def load_vars(self):
        try:
            self.get_path_and_full_conf()
            self.get_io_paths()
            self.vars_global = {}
            self.vars_common = {}
            self.vars_conf = {}
            # First load the globals
            vars_global = self.load_vars_file(self.input_path + 'ccinfra.global')
            # Then the commons
            vars_common = self.load_vars_file(self.input_path + 'ccinfra.common')
            # Finally the local conf (overrides will be down-top)
            vars_conf = self.load_vars_file(self.input_conf)
        finally:
            self.vars_data = {'vars': dict(vars_global['vars'].items() +
                                           vars_common['vars'].items() +
                                           vars_conf['vars'].items())
                             }
            return self.vars_data    

    def build_file(self, input_conf):
        try:
            # I assume that conf/srv (two dirs) are always prepended to the path
            self.input_conf = input_conf
            self.get_path_and_full_conf()
            self.get_io_confs()
            self.get_io_paths()
            
            self.fin = open(input_conf)
            self.fout = self.open_or_create_dir()
    
            vars_data = self.load_vars()
            #pprint(vars_data)
            
            js = json.dumps(vars_data, sort_keys=True,
                            indent=4, separators=(',', ' : '))
            print js
            try:
                for line in self.fin:
                    try:
                        out_line = line
                        s = Template(line)
                        out_line = s.substitute(vars_data['vars'])
                        self.fout.write(out_line)
                    except KeyError, err:
                        print 'ERROR: ' + str(err) + ' variable is missing'
            finally:
                self.fout.close()
                self.fin.close()
            return self.output_conf
        except Exception, e:
            raise e