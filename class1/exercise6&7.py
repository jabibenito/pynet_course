import yaml
import json
from pprint import pprint as pp

my_list = []

while True:
    x = raw_input("Enter num or text to add to list or press enter to finish: ")
    if not x: break
    my_list.append(x)

my_list.append({})

while True:
    y = raw_input("Enter the name of the key in the list or press enter to finish: ")
    z = raw_input("Enter the value of the key or press enter to finish: ")
    if not y: break
    if not z: break
    my_list[-1][y] = z

print "----------------------------------"
print "Importing this list to YAML format"
print "----------------------------------"

with open ("computer_details.yml", "w") as f:
    f.write(yaml.dump(my_list, default_flow_style=False))

print yaml.dump(my_list, default_flow_style=False)

print "----------------------------------"
print "Importing this list to JSON format"
print "----------------------------------"


with open("computer_details.json", "w") as f:
    json.dump(my_list, f)

pp(my_list)








