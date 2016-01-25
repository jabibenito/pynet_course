# 2. telnetlib
#
#     a. Write a script that connects using telnet to the pynet-rtr1 router.
#     Execute the 'show ip int brief' command on the router and return the output.
#
# Try to do this on your own (i.e. do not copy what I did previously). You should be able to do this by using the following items:
#
# telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
# remote_conn.read_until(<string_pattern>, TELNET_TIMEOUT)
# remote_conn.read_very_eager()
# remote_conn.write(<command> + '\n')
# remote_conn.close()


import telnetlib
import socket
import time

ip_addr = "50.76.53.27"
username = 'pyclass'
password = '88newclass'
TELNET_PORT = 23
TELNET_TIMEOUT = 5

try:
    remote_conn = telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)

except socket.timeout:
    print "Unreachable Host"

remote_conn.read_until("sername:", TELNET_TIMEOUT)
remote_conn.write(username + "\n")
remote_conn.read_until("assword:", TELNET_TIMEOUT)
remote_conn.write(password + "\n")

remote_conn.read_very_eager()


remote_conn.write("show ip int brief" + "\n")

time.sleep(1)
output = remote_conn.read_very_eager()
print output

remote_conn.close()
