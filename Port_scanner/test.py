import os
import json



# Open json with common ports and services
base_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(base_dir, "common_ports.json") 
with open(path, 'r') as file:
    common_ports_dictionnary = json.load(file)
# print(common_ports_dictionnary)
# smtp = common_ports_dictionnary.get("25")

open_ports = [135, 139]
for port in open_ports: 
    service = common_ports_dictionnary.get(str(port))
    print(service)