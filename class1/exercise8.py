# Write a Python program using ciscoconfparse that parses this config file.
# Note, this config file is not fully valid (i.e. parts of the configuration are missing).
# The script should find all of the crypto map entries in the file (lines that begin with 'crypto map CRYPTO') and for each crypto map entry print out its children.

from ciscoconfparse import CiscoConfParse

# Adding cisco configuration file to variable
cisco_cfg = CiscoConfParse("cisco_ipsec.txt")

# Create a varible with lines of the file thay start with crypto map CRYPTO
crypto_map = cisco_cfg.find_objects(r"^crypto map CRYPTO")

print "--------------------------------------------------------------"
print "Printing crypto maps that start with crypto map CRYPTO"
print "--------------------------------------------------------------"


# Print all lines starting with crypto map Crypto and their respective children
for crypto in crypto_map:
    print crypto.text
    for child in crypto.children:
       print child.text