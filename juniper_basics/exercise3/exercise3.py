#!/usr/bin/env python

from jnpr.junos import Device
from jnpr.junos.op.routes import RouteTable
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

    table = RouteTable(a_device)
    table.get()

    print
    print "Juniper SRX Routing Table"
    print

    for route, rtable in table.items():
        rtable = dict(rtable)
        #print stats
        nexthop = rtable['nexthop']
        age = rtable['age']
        via = rtable['via']
        protocol = rtable['protocol']
        print route
        print " NextHop %s" % (nexthop)
        print " age %s" % (age)
        print " via %s" % (via)
        print " protocol %s" % (protocol)
        print

if __name__ == "__main__":
    main()