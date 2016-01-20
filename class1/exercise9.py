# Find all of the crypto map entries that are using PFS group2


from ciscoconfparse import CiscoConfParse

# Adding cisco configuration file to variable
cisco_cfg = CiscoConfParse("cisco_ipsec.txt")

print "----------------------------------------------------"
print "Printing crypto maps that are using PFS group 2"
print "----------------------------------------------------"


pfs_group = cisco_cfg.find_objects_w_child(parentspec=r"^crypto map CRYPTO", childspec=r"pfs group2")
#print pfs_group

for pfs in pfs_group:
   print pfs.text
#   for child in pfs.children:
#       print child.text

