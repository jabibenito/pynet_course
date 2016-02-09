from getpass import getpass
from netmiko import ConnectHandler


def main():

    password = getpass()

    pynet_rtr2 = {'device_type': 'cisco_ios', 'ip': '50.76.53.27', 'username': 'pyclass', 'password': password, 'port': 8022}

    ssh_connection = ConnectHandler(**pynet_rtr2)
    ssh_connection.config_mode()
    logging_command = ['logging buffered 20031']
    ssh_connection.send_config_set(logging_command)

    output = ssh_connection.send_command('show run | inc logging buffered')
    outp = output.split(' ')

    print "The new size of logging buffered is %s" % outp[2]

if __name__ == "__main__":
    main()




