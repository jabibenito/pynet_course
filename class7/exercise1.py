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
import sys

# Creating the connection
pynet_sw1 = pyeapi.connect_to("pynet-sw1")


# Executing 'show interfaces' command in enable mode.
running_config = pynet_sw1.enable('show interfaces')
running_config_dict = running_config[0]

interfaces = running_config_dict['result']
ipv4_interfaces = interfaces['interfaces']
interfaces = ipv4_interfaces.keys()

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
    sys.exit()
