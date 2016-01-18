# Using ciscoconfparse find the crypto maps that are not using AES (based-on the transform set name).
# Print these entries and their corresponding transform set name.

import re
from ciscoconfparse import CiscoConfParse

# Adding cisco configuration file to variable
cisco_cfg = CiscoConfParse("cisco_ipsec.txt")

print "----------------------------------------------------"
print "Printing crypto maps that are not using AES"
print "----------------------------------------------------"

aes_group = cisco_cfg.find_objects_wo_child(parentspec=r"^crypto map CRYPTO", childspec=r"transform-set AES")
#print aes_group

for aes in aes_group:
   print aes.text
   for child in aes.children:
        print child.text

