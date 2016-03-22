#!/usr/bin/env python
# Optional bonus question
# --use a queue to get the output data back from the child processes in question #7.
# Print this output data to the screen in the main process.
# amount of time executing with processes and queues : 0:00:07.893882

from datetime import datetime
from multiprocessing import Process, Queue

from netmiko import ConnectHandler


from net_system.models import NetworkDevice, Credentials
import django


def show_version(n_device, output_queue):
    output_dict = {}
    creds = n_device.credentials
    remote_conn = ConnectHandler(device_type=n_device.device_type, ip=n_device.ip_address,
                                 username=creds.username, password=creds.password,
                                 port=n_device.port)

    output = '*' * 100
    output += remote_conn.send_command("show version")
    output += '*' * 100
    output_dict[n_device.device_name] = output
    output_queue.put(output_dict)

def main():
    django.setup()

    start_time = datetime.now()

    output_queue = Queue(maxsize=20)
    network_devices = NetworkDevice.objects.all()

    processes = []
    for n_device in network_devices:
        # Creating and starting process with show_version function
        my_process = Process(target=show_version, args=(n_device, output_queue))
        my_process.start()
        processes.append(my_process)

    for n_proc in processes:
        n_proc.join()

    while not output_queue.empty():
        my_dict = output_queue.get()
        for key, value in my_dict.iteritems():
            print key
            print value


    total_time = datetime.now() - start_time
    print "Total time is :{}".format(total_time)

if __name__ == "__main__":
    main()

