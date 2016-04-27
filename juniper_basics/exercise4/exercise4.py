#!/usr/bin/env python

from jnpr.junos import Device
from jnpr.junos.utils.config import Config
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

    cfg = Config(a_device)

    print "Changing hostname with set command"
    cfg_load = cfg.load("set system host-name batz-jnpr-srx1", format ="set", merge=True)
    print cfg.diff()
    print
    print "Doing rollback"
    cfg.rollback(0)


    print "Changing hostname with conf method "
    cfg_load_conf = cfg.load(path='hostname.conf', format='text', merge=True)
    print cfg.diff()
    print
    print "Doing rollback"
    cfg.rollback(0)


    print "Changing hostname with xml method"
    cfg_load_xml = cfg.load(path='hostname.xml', format='xml', merge=True)
    print cfg.diff()
    print

    print "Doing changes"
    cfg.commit()
    print


if __name__ == "__main__":
    main()