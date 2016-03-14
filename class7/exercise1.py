# Use Arista's eAPI to obtain 'show interfaces' from the switch.
# Parse the 'show interfaces' output to obtain the 'inOctets' and 'outOctets'
# fields for each of the interfaces on the switch.  Accomplish this using Arista's pyeapi.
# ~/.eapi.conf
# [connection:pynet-sw1]
# username: eapi
# password: 99saturday
# host: 50.76.53.27
# port: 8243
# transport: https

import pyeapi
from pprint import pprint
import sys

# Creating the connection
pynet_sw1 = pyeapi.connect_to("pynet-sw1")
#print pynet_sw1

# Executing 'show interfaces' command in enable mode.
running_config = pynet_sw1.enable('show interfaces')
#for line in running_config:
#    pprint(line)

#print len(running_config)

running_config_dict = running_config[0]
#print running_config_dict.items()

interfaces = running_config_dict['result']

#print interfaces.keys()

ipv4_interfaces = interfaces['interfaces']
#inOctects = interfaces['inOctets']
#outOctets = interfaces['outOctets']

#print len(ipv4_interfaces)

interfaces = ipv4_interfaces.keys()
#print inOctects
#print outOctets

#pprint(ipv4_interfaces.keys())

try:
    for line in interfaces:
        interface = line
        interface_ethernet = ipv4_interfaces[interface]
        Interface_Counters = interface_ethernet['interfaceCounters']
        inOctets = Interface_Counters['inOctets']
        outOctets = Interface_Counters['outOctets']
        print "----------------------------------"
        print "Interface %s" % interface
        print "Number of inOctes is %s" % inOctets
        print "Number of outOctets is %s" % outOctets
        print "----------------------------------"

except KeyError:
    sys.exit

#interface_ethernet = ipv4_interfaces['Ethernet2']
#print interface_ethernet.keys()
#Interface_Counters = interface_ethernet['interfaceCounters']
#print Interface_Counters
#inOctets = Interface_Counters['inOctets']
#print inOctets
#outOctets = Interface_Counters['outOctets']
#print outOctets






