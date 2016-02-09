from netmiko import ConnectHandler
from getpass import getpass

def main():

    password = getpass()

    pynet_rtr1 = {'device_type': 'cisco_ios', 'ip': '50.76.53.27', 'username': 'pyclass', 'password': password, 'port': 22}
    pynet_rtr2 = {'device_type': 'cisco_ios', 'ip': '50.76.53.27', 'username': 'pyclass', 'password': password, 'port': 8022}
    pynet_jnpr_srx1 = {'device_type': 'juniper', 'ip': '50.76.53.27', 'username': 'pyclass', 'password': password, 'port': 9822}

    for ssh in pynet_rtr1,pynet_rtr2,pynet_jnpr_srx1:
        ssh_connection = ConnectHandler(**ssh)
        output = ssh_connection.send_command('show arp')
        print output

if __name__ == "__main__":
    main()