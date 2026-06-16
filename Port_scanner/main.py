from scanner import scanner
from report import report


# For the moment, the IP is in the script. 
# Later, it will be an arg passed in the CLI
ip_address = "192.168.129.2"

# Calculate the duration of the scan
open_ports, scan_starts, scan_stops = scanner(ip_address)
duration_scan = scan_stops - scan_starts
duration_seconds = duration_scan.total_seconds()
print(open_ports)
print(f"Duration of the scan : {duration_seconds} s.")
print(f"Duration in minutes : {duration_seconds / 60} min.")

# write the report
report(ip_address, open_ports, duration_seconds)
