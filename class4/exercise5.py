from getpass import getpass
import time
from netmiko import ConnectHandler

password = getpass()

pynet_rtr2 = {'device_type': 'cisco_ios', 'ip': '50.76.53.27', 'username': 'pyclass', 'password': password, 'port': 8022}

ssh_connection = ConnectHandler(**pynet_rtr2)
time.sleep(2)

ssh_connection.config_mode()
output = ssh_connection.find_prompt()

print "The current state of the prompt is %s" % output



