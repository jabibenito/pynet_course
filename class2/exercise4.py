# 4. SNMP Basics
#
#     a. Create an 'SNMP' directory in your home directory.
#
# $ mkdir SNMP
# $ cd SNMP
#
#     b. Verify that you can import the snmp_helper library.  This is a small library that I created to simplify aspects of PySNMP.
#
# $ python
# Python 2.7.5 (default, Feb 11 2014, 07:46:25)
# [GCC 4.8.2 20140120 (Red Hat 4.8.2-13)] on linux2
# Type "help", "copyright", "credits" or "license" for more information.
# >>>
# >>> import snmp_helper
#
# c. Create a script that connects to both routers (pynet-rtr1 and pynet-rtr2) and prints out both the MIB2 sysName and sysDescr.

import snmp_helper

COMMUNITY_STRING = "galileo"
RTR1_SNMP_PORT = 7961
RTR2_SNMP_PORT = 8061
IP = "50.76.53.27"

RTR1 = (IP, COMMUNITY_STRING, RTR1_SNMP_PORT)
RTR2 = (IP, COMMUNITY_STRING, RTR2_SNMP_PORT)

sysName = "1.3.6.1.2.1.1.5.0"
sysDescr = "1.3.6.1.2.1.1.1.0"


## Getting snmp info

snmp_SysName_rtr1 = snmp_helper.snmp_get_oid(RTR1, oid=sysName)
snmp_SysDescr_rtr1 = snmp_helper.snmp_get_oid(RTR1, oid=sysDescr)

snmp_SysName_rtr2 = snmp_helper.snmp_get_oid(RTR2, oid=sysName)
snmp_SysDescr_rtr2 = snmp_helper.snmp_get_oid(RTR2, oid=sysDescr)

## Saving SNMP info in a variable

snmp_RTR1_output_SysName = snmp_helper.snmp_extract(snmp_SysName_rtr1)
snmp_RTR1_output_SysDescr = snmp_helper.snmp_extract(snmp_SysDescr_rtr1)

snmp_RTR2_output_SysName = snmp_helper.snmp_extract(snmp_SysName_rtr2)
snmp_RTR2_output_SysDescr = snmp_helper.snmp_extract(snmp_SysDescr_rtr2)


print "*******************  " + snmp_RTR1_output_SysName + "  *********************"
print snmp_RTR1_output_SysDescr
print "*******************  " + snmp_RTR2_output_SysName + "  *********************"
print snmp_RTR2_output_SysDescr



