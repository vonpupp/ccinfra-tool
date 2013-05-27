#!/usr/bin/python

from string import Template
import json
from pprint import pprint
import os

OUTDIR = 'out/'


#class MyTemplate(Template):
#    delimiter = '{{'
#    pattern = r'''
#    \{\{(?:
#    (?P<escaped>\{\{)|
#    (?P<named>[_a-z][_a-z0-9]*)\}\}|
#    (?P<braced>[_a-z][_a-z0-9]*)\}\}|
#    (?P<invalid>)
#    )
#    '''

# class MyTemplate(string.Template):
#     delimiter = '%'
#     idpattern = '[a-z]+_[a-z]+'


class FileBuilder():
    def FileBuilder(self):
        self.conf_file = ''
        self.conf_path = ''
        self.input_path = ''
        self.output_path = ''

    def set_out_path(self, output_path):
        self.output_path = output_path

    def set_in_path(self, input_path):
        self.input_path = input_path
        self.load_initial_vars()
    
#     def set_prefix_path(self, prefix_path):
#         self.input_path = input_path
#         'conf/srv/etc/
#         
#         'conf/srv/'
#         'conf/srv/etc/dhcpd.conf'

    def open_or_create_dir(self):
        self.input_path, self.output_path = self.get_io_paths()
        result = None
        try:
            result = open(self.output_conf, 'w')
        except:
            os.makedirs(self.output_path)
        return result

    def get_path_and_full_conf(self):
        self.conf_file = self.input_conf.split('/')[-1]
        leading_path = self.input_conf.rsplit('/', 1)[0]
        if leading_path.startswith('/'):
            leading_path = leading_path[1:]
        self.conf_path = self.input_path + leading_path

        return self.conf_path, self.conf_file

    def get_io_confs(self):
        self.output_conf = self.output_path + self.conf_file
        #self.relative_etc_conf = self.input_conf.split('etc/')[1]
        #self.output_conf = OUTDIR + 'etc/' + self.relative_etc_conf

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
            return {'vars': {}}

    def load_initial_vars(self):
        try:
            self.vars_global = {}
            self.vars_common = {}
            # First load the globals
            self.vars_global = self.load_vars_file(self.input_path +
                                                   'ccinfra.global')
            # Then the commons
            self.vars_common = self.load_vars_file(self.input_path +
                                                   'ccinfra.common')
        finally:
            self.vars_initial = {'vars': dict(self.vars_global['vars'].items() +
                                            self.vars_common['vars'].items())}
            return self.vars_initial

    def load_vars(self):
        try:
            #self.get_path_and_full_conf()
            #self.get_io_paths()
            self.vars_conf = {}
            # This might override will common and global vars
            self.vars_conf = self.load_vars_file(self.input_conf)
        finally:
            self.vars_data = {'vars': dict(self.vars_initial['vars'].items() +
                                           self.vars_conf['vars'].items())}
            return self.vars_data

    def set_file_in(self, input_conf):
        try:
            # I assume that conf/srv (two dirs) are
            # always prepended to the path
            self.input_conf = input_conf
            self.get_path_and_full_conf()
            self.get_io_confs()
            self.get_io_paths()

            print self.input_conf
            print self.output_conf
        except Exception, e:
            raise e

    def build_file(self, input_conf):
        try:
            # I assume that conf/srv (two dirs) are
            # always prepended to the path
            self.set_file_in(input_conf)
            
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
                        #out_line = line
                        s = Template(line)
                        out_line = s.substitute(vars_data['vars'])
                    except KeyError, err:
                        print 'ERROR: ' + str(err) + ' variable is missing'
                    except ValueError, err:
                        out_line = line
                    finally:
                        self.fout.write(out_line)
            finally:
                self.fout.close()
                self.fin.close()
            return self.output_conf
        except Exception, e:
            raise e
