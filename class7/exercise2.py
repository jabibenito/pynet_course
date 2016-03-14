#!/usr/bin/env python

# Using Arista's pyeapi, create a script that allows you to add a VLAN (both the VLAN ID and the VLAN name).
# Your script should first check that the VLAN ID is available and only add the VLAN if it doesn't already exist.
# Use VLAN IDs between 100 and 999.  You should be able to call the script from the command line as follows:
#
#       python eapi_vlan.py --name blue 100     # add VLAN100, name blue
#
# If you call the script with the --remove option, the VLAN will be removed.
#
#    python eapi_vlan.py --remove 100          # remove VLAN100
#
# Once again only remove the VLAN if it exists on the switch.
# You will probably want to use Python's argparse to accomplish the argument processing.
#
# In the lab environment, if you want to directly execute your script,
# then you will need to use '#!/usr/bin/env python' at the top of the script (instead of '!#/usr/bin/python').
#
# ~/.eapi.conf
# [connection:pynet-sw1]
# username: eapi
# password: 99saturday
# host: 50.76.53.27
# port: 8243
# transport: https

import pyeapi
import argparse
from pprint import pprint

parser = argparse.ArgumentParser(description='Script configure vlan id and vlan name in Arista switch')

# Add arguments
parser.add_argument(
    '-n', '--name', type=str, help='Vlan name', action='store', dest='vlan_name')
parser.add_argument(
    '-v', '--vlan', type=str, help='Vlan number', action='store', dest='vlan_id')
parser.add_argument(
    '-d', '--remove', type=str, help='Delete Vlan', action='store', dest='delete_vlan')

results = parser.parse_args()
var_vlan_name = results.vlan_name
var_vlan_id = results.vlan_id
var_del_vlan = results.delete_vlan

if var_del_vlan != None:
    delete_vlan = 'no vlan %s' % results.delete_vlan
    pynet_sw1 = pyeapi.connect_to("pynet-sw1")
    vlan_command = pynet_sw1.enable("show vlan")
    vlan_dict = vlan_command[0]
    vlans = vlan_dict['result']
    vlan_list = vlans['vlans']

    if var_del_vlan in vlan_list.keys():
        pynet_sw1 = pyeapi.connect_to("pynet-sw1")
        pynet_sw1.config(delete_vlan)
        print "Vlan removed"

    else:
        print "Vlan id does not exist"

if var_vlan_name or var_vlan_id != None:
    vlan_name = 'name %s' % results.vlan_name
    vlan_id = 'vlan %s' % results.vlan_id
    pynet_sw1 = pyeapi.connect_to("pynet-sw1")
    vlan_command = pynet_sw1.enable("show vlan")
    vlan_dict = vlan_command[0]
    vlans = vlan_dict['result']
    vlan_list = vlans['vlans']

    cmds=[vlan_id, vlan_name]

    if var_vlan_id in vlan_list.keys():
        print "Vlan id exists"

    else:
        pynet_sw1 = pyeapi.connect_to("pynet-sw1")
        pynet_sw1.config(cmds)

