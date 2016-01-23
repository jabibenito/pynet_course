import snmp_helper ## If we import snmp_helpder directly, we have to add module name before fucntions in the variables.

# from snmp_helper import snmp_get_oid,snmp_extract.
# If we import only determined functions. We don't have to add module name before funtions in the variables.


COMMUNITY_STRING = 'galileo'
SNMP_PORT = 8061
IP = '50.76.53.27'

device = (IP, COMMUNITY_STRING, SNMP_PORT)

OID = '1.3.6.1.2.1.1.1.0'

snmp_data = snmp_helper.snmp_get_oid(device, oid=OID)
# snmp_data = snmp_get_oid(device, oid=OID)

output = snmp_helper.snmp_extract(snmp_data)
# output = snmp_extract(snmp_data)


print output
