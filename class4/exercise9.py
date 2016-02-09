from getpass import getpass
import threading
import time
from netmiko import ConnectHandler

def connect(host):

    ssh_connection = ConnectHandler(**host)
    output = ssh_connection.send_command('show arp')
    hostname = ssh_connection.find_prompt()
    time.sleep(1)

    print '*' * 35 + " ARP Table from device %s " % hostname + '*' * 35
    print output
    print '*' * 105

def main():

    password = getpass()

    pynet_rtr1 = {'device_type': 'cisco_ios', 'ip': '50.76.53.27', 'username': 'pyclass', 'password': password, 'port': 22}
    pynet_rtr2 = {'device_type': 'cisco_ios', 'ip': '50.76.53.27', 'username': 'pyclass', 'password': password, 'port': 8022}
    pynet_jnpr_srx1 = {'device_type': 'juniper', 'ip': '50.76.53.27', 'username': 'pyclass', 'password': password, 'port': 9822}

    hosts = [pynet_rtr1, pynet_rtr2, pynet_jnpr_srx1]

    threads = []
    for h in hosts:
        t = threading.Thread(target=connect, args=(h,))
        t.start()
        threads.append(t)
    for t in threads:
        t.join

if __name__ == "__main__":
    main()