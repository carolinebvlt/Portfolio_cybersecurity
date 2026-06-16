import os
import json


def report(open_ports, duration_scan) :

    # Open json with common ports and services
    base_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base_dir, "common_ports.json") 
    with open(path, 'r') as file:
        common_ports_dictionnary = json.load(file)

    # For each open port, find the service name
    for port in open_ports: 
        service = common_ports_dictionnary.get(str(port))
        print(service)
    
    # Display duration of the scan
    print(f"Scan duration : {duration_scan}")