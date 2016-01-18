from ciscoconfparse import CiscoConfParse

# Adding cisco configuration file to variable
cisco_cfg = CiscoConfParse("cisco_ipsec.txt")

# Create a varible with lines of the file thay start with crypto map CRYPTO
crypto_map = cisco_cfg.find_objects(r"^crypto map CRYPTO")

#print "-----------------------------------------------"
#print "We are going to find cryptos thay start with crypto map CRYPTO"
#print "-----------------------------------------------"


# Print all lines starting with crypto map Crypto and their respective children
#for crypto in crypto_map:
#    print crypto.text
#    for child in crypto.children:
#       print child.text

#print "-----------------------------------------------"
#print "We are going to find PFS group 2 configurations"
#print "-----------------------------------------------"

pfs_group = cisco_cfg.find_objects_w_child(parentspec=r"^crypto map CRYPTO", childspec=r"pfs group2")
#print pfs_group

for pfs in pfs_group:
   print pfs.text
#   for child in pfs.children:
#        print child.text





print "----------------------------------------------------"
print "We are going to find all Cryptos that do not use AES"
print "----------------------------------------------------"

aes_group = cisco_cfg.find_objects_wo_child(parentspec=r"^crypto map CRYPTO", childspec=r"transform-set AES")
#print aes_group

for aes in aes_group:
   print aes.text
   for child in aes.children:
        print child.text