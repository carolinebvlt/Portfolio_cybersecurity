import os
import json
from datetime import datetime

def report(ip_address, open_ports, duration_seconds) :

    # Init a list of lines for the report (join later)
    report_lines = [];

    report_lines.append("##############################")
    report_lines.append("###### PORT SCAN REPORT ######")
    report_lines.append("##############################\n")

    report_lines.append(f"Analyzed IP address : {ip_address}\n")

    report_lines.append(f"Report date : {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n")

    report_lines.append(f"Scan duration : {round(duration_seconds, 2)} s.")
    report_lines.append(f"Scan duration :{round(duration_seconds/60, 2)} min.\n")

    # Open json with common ports and services
    base_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base_dir, "common_ports.json") 
    with open(path, 'r') as file:
        common_ports_dictionnary = json.load(file)

    # For each open port, find the service name
    report_lines.append("Open ports : \n")
    
    for port in open_ports: 
        
        service = common_ports_dictionnary.get(str(port))
        
        # If that port/service is in the json dictionnary, add it to the report
        if service != None :
            report_lines.append(f"{port} : {service}")
        else :
            report_lines.append(f"{port}")
    
    # Generation report 
    report_name = f"port_scan_report_{datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}.txt"
    base_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base_dir, report_name)

    with open(path, "w") as file :
        file.write("\n".join(report_lines))
    