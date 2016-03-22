#!/usr/bin/env python
# Use Netmiko to connect to each of the devices in the database.
# Execute 'show version' on each device.
# Calculate the amount of time required to do this.
# amount of time executing sequentially is: 0:00:49.783342

from datetime import datetime
from netmiko import ConnectHandler


from net_system.models import NetworkDevice, Credentials
import django

def main():
    django.setup()

    start_time = datetime.now()

    network_devices = NetworkDevice.objects.all()
    for n_device in network_devices:
        print n_device
        creds = n_device.credentials

        remote_conn = ConnectHandler(device_type=n_device.device_type, ip=n_device.ip_address,
                                     username=creds.username, password=creds.password,
                                     port=n_device.port)

        print '*' * 100
        print remote_conn.send_command("show version")
        print '*' * 100

    total_time = datetime.now() - start_time
    print "Total time is :{}".format(total_time)

if __name__ == "__main__":
    main()
