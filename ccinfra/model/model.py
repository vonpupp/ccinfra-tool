#!/usr/bin/env python2

import os
from filebuilder import FileBuilder


class GeneralSetup():
    """
    Attributes:
    """

    def __init__(self):
        pass

    def is_opensuse_host():
        return os.file_exists('/etc/SuSE-release')


class ServerSetup(GeneralSetup):
    """
    Attributes:
    """
    root_conf_out = '/etc'
    root_conf_in = 'conf/srv/'
    fb = None

    def __init__(self):
        self.fb = FileBuilder()
        self.fb.set_in_path(self.root_conf_out)
        self.fb.set_out_path(self.root_conf_in)

    def network_setup(self):
        pass

    def packages_setup(self):
        pass

    def vpn_setup(self):
        pass

    def deploy_setup(self):
        pass

    def ntp_setup(self):
        pass

    def isc_dhcpd_setup(self):
        # Explicit paths are better than implicit
        self.fb.build_file('/etc/dhcpd.conf')

    def named_keys_setup(self):
        self.fb.build_file('/etc/dhcpd.conf')

    def named_setup(self):
        self.fb.build_file('named.conf')
        self.fb.build_file('named.conf.include')

    def openldap_setup(self):
        pass

    def ccbsist_setup(self):
        pass

    def nfs_setup(self):
        pass

    def samba_setup(self):
        pass

    def firewall_setup(self):
        pass

    def setup_all(self):
        pass


class ClientSetup(GeneralSetup):
    """
    Attributes:
    """
    root_conf = '.conf/cli/'

    def __init__(self):
        pass

    def network_setup(self):
        pass

    def packages_setup(self):
        pass

    def ntp_setup(self):
        pass

    def ldap_setup(self):
        pass

    def autofs_setup(self):
        pass

    def firewall_setup(self):
        pass

    def setup_all(self):
        pass
