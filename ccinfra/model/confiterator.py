#!/usr/bin/python

import os


class ConfIterator():
    def FileIterator(self):
        self.input_path = ''

    def set_input_path(self, input_path):
        self.input_path = input_path

    def files(self):
        for dirname, dirnames, filenames in os.walk(self.input_path):
            if '.git' in dirnames:
                dirnames.remove('.git')
            for subdirname in dirnames:
                pass
            for filename in filenames:
                if not filename.endswith('.vars'):
                    yield os.path.join(dirname, filename)
