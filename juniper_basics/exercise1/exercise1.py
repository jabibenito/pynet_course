#!/usr/bin/env python

from jnpr.junos import Device
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
    pprint(a_device.facts)


if __name__ == "__main__":
    main()