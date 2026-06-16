import socket
from datetime import datetime

def scanner(ip_address):

    # Create an empty list for open ports
    open_ports = []

    # Timestamp scan starts
    scan_starts = datetime.now()


    # For loop to scan from port 1 to 1024 included

    for port in range(1, 1025) :
        
        # Create a socket with a timeout and try to connect
        my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        my_socket.settimeout(0.2)
        result = my_socket.connect_ex((ip_address, port))
        my_socket.close()
        
        # If the port is open
        if result == 0 :
            open_ports.append(port)
            print(f"Open port : {port}")
        
        # If the port is closed
        else :
            print(f"Closed port : {port}")

    # Timestamp scan stops
    scan_stops = datetime.now()

    return open_ports, scan_starts, scan_stops