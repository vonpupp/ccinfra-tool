#!/usr/bin/env python2

import os
from filebuilder import FileBuilder
from subprocess import call


class GeneralSetup():
    """
    Attributes:
    """

    def __init__(self):
        pass

    def is_opensuse_host(self):
        return os.file_exists('/etc/SuSE-release')


class ServerSetup(GeneralSetup):
    """
    Attributes:
    """

    def __init__(self):
        self.fb = FileBuilder()
        self.set_in_path('conf/')
        self.set_out_path('out/')

    def set_in_path(self, conf_in):
        # Assumed that server config will always be at:
        # conf_in/srv
        self.root_conf_in = conf_in
        self.fb.set_in_path(self.root_conf_in)

    def set_out_path(self, conf_out):
        self.root_conf_out = conf_out
        self.fb.set_out_path(self.root_conf_out)

    def build_file(self, conf_in):
        if conf_in.startswith('/'):
            conf_in = conf_in[1:]
        conf = self.root_conf_in + conf_in
        self.fb.build_file(conf)

    def network_setup(self):
        pass

    def packages_setup(self):
        pass

    def vpn_setup(self):
        pass

    def deploy_setup(self):
        pass

    def ntp_setup(self):
        self.build_file('/etc/ntp.conf')

    def isc_dhcpd_setup(self):
        # Explicit (relative to etc) paths are better than implicit
        self.build_file('/etc/dhcpd.conf')
        #call(['service', 'dhcpd restart'])

    def named_keys_setup(self):
        self.build_file('/etc/rndc.key')

    def named_setup(self):
        self.build_file('/etc/named.conf')
        self.build_file('/etc/named.conf.include')
        self.build_file('/etc/named.d/dns.key')
        self.build_file('/etc/named.d/forwarders.conf')
        self.build_file('/etc/named.d/rndc-access.conf')

    def nfs_setup(self):
        self.build_file('/etc/exports')

    def openldap_setup(self):
        self.build_file('/etc/ldap.conf')
        self.build_file('/etc/nsswitch.conf')
        self.build_file('/etc/pam.d/common-account-pc')
        self.build_file('/etc/pam.d/common-auth-pc')
        self.build_file('/etc/pam.d/common-password-pc')
        self.build_file('/etc/pam.d/common-session-pc')

    def ldap_users_setup(self):
        pass

    def ccbsist_setup(self):
        pass

    def samba_setup(self):
        self.build_file('/etc/samba/smb.conf')

    def squid_setup(self):
        self.build_file('/etc/squid/squid.conf')

    def firewall_setup(self):
        pass

    def setup_default_pattern(self):
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
