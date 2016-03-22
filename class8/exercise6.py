#!/usr/bin/env python
# Use threads and Netmiko to execute 'show version' on each device in the database.
# Calculate the amount of time required to do this.
# What is the difference in time between executing
# 'show version' sequentially versus using threads?
# amount of time executing with threads is : 0:00:07.653559

from datetime import datetime
import threading

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

    network_devices = NetworkDevice.objects.all()
    for n_device in network_devices:
        # Creating and starting thread with show_version function
        network_thread = threading.Thread(target=show_version, args=(n_device,))
        network_thread.start()

    main_thread = threading.currentThread()
    for n_thread in threading.enumerate():
        if n_thread != main_thread:
            print n_thread
            n_thread.join()


    total_time = datetime.now() - start_time
    print "Total time is :{}".format(total_time)

if __name__ == "__main__":
    main()
