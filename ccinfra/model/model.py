#!/usr/bin/env python3

class GeneralSetup():
    """
    Attributes:
    """
    
    def __init__(self):
        pass

    def is_opensuse_host():
        pass

    def replace_copy(self, input_file, input_expr, output_file, output_expr):
        f = open(input_file)
        contents = f.read()
        replaced_contents = contents.replace(input_expr, output_expr)

class ServerSetup(GeneralSetup):
    """
    Attributes:
    """
    root_conf = '.conf/srv/'
    
    def __init__(self):
        pass
    
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

    def dhcp_setup(self):
        pass
    
    def dns_setup(self):
        pass
    
    def ldap_setup(self):
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
