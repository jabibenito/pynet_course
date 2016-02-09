#!/usr/bin/env python

import pexpect
import sys
from getpass import getpass
import time

def main():
    ip_addr = '50.76.53.27'
    username = 'pyclass'
    port = 8022
    password = getpass()

    # ssh -l pyclass 50.76.53.27 -p 8022
    ssh_conn = pexpect.spawn('ssh -l {} {} -p {}'.format(username, ip_addr, port))

    #Useful for debugging the session
    #ssh_conn.logfile = sys.stdout
    ssh_conn.timeout = 3
    ssh_conn.expect('ssword:')
    time.sleep(1)
    ssh_conn.sendline(password)

    ssh_conn.expect('#')

    ssh_conn.sendline('terminal lenght 0')
    ssh_conn.expect('#')

    ssh_conn.sendline('configure terminal')
    time.sleep(1)
    ssh_conn.expect('#')

    ssh_conn.sendline('logging buffered 20000')
    time.sleep(1)
    ssh_conn.expect('#')

    ssh_conn.sendline('exit')
    time.sleep(1)
    ssh_conn.expect('#')

    ssh_conn.sendline('show running-config')
    time.sleep(2)
    ssh_conn.expect('no logging console')

    # Print the output of the show ip int brief command.
    print ssh_conn.before

if __name__ == "__main__":
    main()