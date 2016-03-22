#!/usr/bin/env python
# Exercise 6 :Use threads and Netmiko to execute 'show version' on each device in the database.
#  Calculate the amount of time required to do this.
# What is the difference in time between executing 'show version' sequentially versus using threads?
# Exercise 7. Repeat exercise #6 except use processes.
# amount of time executing with processes is : 0:00:07.671134

from datetime import datetime
from multiprocessing import Process

from netmiko import ConnectHandler


from net_system.models import NetworkDevice, Credentials
import django


def show_version(n_device):
    creds = n_device.credentials
    remote_conn = ConnectHandler(device_type=n_device.device_type, ip=n_device.ip_address,
                                 username=creds.username, password=creds.password,
                                 port=n_device.port)

    print '*' * 100
    print remote_conn.send_command("show version")
    print '*' * 100

def main():
    django.setup()

    start_time = datetime.now()

    processes = []
    network_devices = NetworkDevice.objects.all()
    for n_device in network_devices:
        # Creating and starting thread with show_version function
        network_process = Process(target=show_version, args=(n_device,))
        network_process.start()
        processes.append(network_process)

    for n_proc in processes:
        print n_proc
        n_proc.join()

    total_time = datetime.now() - start_time
    print "Total time is :{}".format(total_time)

if __name__ == "__main__":
    main()
