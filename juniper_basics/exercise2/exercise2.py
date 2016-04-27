#!/usr/bin/env python

from jnpr.junos import Device
from jnpr.junos.op.ethport import EthPortTable
from getpass import getpass
from pprint import pprint


def main():

    pwd = getpass()

    juniper = {
        "host": "50.76.53.27",
        "user": "pyclass",
        "password": pwd
    }

    a_device = Device(**juniper)
    a_device.open()

    ports = EthPortTable(a_device)
    ports.get()

    for eth, stats in ports.items():
        stats = dict(stats)
        #print stats
        interface_status = stats['oper']
        packets_in = stats['rx_packets']
        packets_out = stats['tx_packets']
        print "Interface: %s Interface status: %s In Packets: %s Out Packets: %s" % (eth, interface_status, packets_in, packets_out)


if __name__ == "__main__":
    main()