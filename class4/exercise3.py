# Use Pexpect to retrieve the output of 'show ip int brief' from pynet-rtr2.
#!/usr/bin/env python
import sys
from getpass import getpass
import pexpect

def main():
    ip_addr = '50.76.53.27'
    username = 'pyclass'
    port = 8022
    password = getpass()

    # ssh -l pyclass 50.76.53.27 -p 8022
    ssh_conn = pexpect.spawn('ssh -l {} {} -p {}'.format(username, ip_addr, port))

    # Useful for debugging the session
    # ssh_conn.logfile = sys.stdout
    ssh_conn.timeout = 3
    ssh_conn.expect('ssword:')
    ssh_conn.sendline(password)

    ssh_conn.expect('#')

    ssh_conn.sendline('show ip int brief')
    ssh_conn.expect('#')

    # Print the output of the show ip int brief command.
    print ssh_conn.before

if __name__ == "__main__":
    main()