import paramiko
from getpass import getpass
import time

def main():
    ip_addr = '50.76.53.27'
    username = 'pyclass'
    password = getpass()
    ssh_port = 8022

    remote_conn_pre = paramiko.SSHClient()
    remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    remote_conn_pre.connect(ip_addr, username=username, password=password, look_for_keys=False, allow_agent=False, port=ssh_port)
    remote_conn = remote_conn_pre.invoke_shell()
    output = remote_conn.recv(65535)

    print output

    outp = remote_conn.send("terminal length 0\n")
    time.sleep(2)
    outp = remote_conn.recv(65535)

    remote_conn.send("configure terminal\n")
    time.sleep(2)
    output = remote_conn.recv(65535)

    remote_conn.send("logging buffered 10000\n")
    time.sleep(2)
    output = remote_conn.recv(65535)

    outp = remote_conn.send("exit\n")
    time.sleep(2)
    outp = remote_conn.recv(65535)

    outp = remote_conn.send("show logging\n")
    time.sleep(2)
    outp = remote_conn.recv(65535)
    print outp

if __name__ == "__main__":
    main()