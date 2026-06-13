import os
import re
from collections import Counter
from datetime import datetime

# Open the file named ssh_logs.txt that's in the same directory than this script
base_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(base_dir, "ssh_logs.txt")

with open(path, "r") as file:
    logs = file.readlines()

# Init a list of dictionnaries (one dict for each log)
list_dict_logs = []


for log in logs :

    # Foreach log, create a dictionnary with :
    # timestamp, host, service, event, user, IP, port (client), protocol

    # find the timestamp, user, and IP with regex
    timestamp_match = re.search(r"^[A-Z][a-z]{2}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2}", log)
    user_match = re.search(r"for (\w+)", log)
    ip_match = re.search(r"\d+\.\d+\.\d+\.\d+", log)
    
    # find the event 'Accepted' or 'Failed'
    event = None
    if 'Accepted password' in log :
        event = "Accepted password"
    elif 'Failed password' in log :
        event = "Failed password"
    
    # Find host, service, port and protocol with split() (all logs have the same structure)
    splited_log = log.split()

    # create the dictionnary and add it to the list of dict
    list_dict_logs.append({
        "timestamp" : timestamp_match.group() if timestamp_match else None,
        "user" : user_match.group(1) if user_match else None,
        "ip" : ip_match.group() if ip_match else None,
        "event": event,
        "host": splited_log[3],
        "service" : splited_log[4],
        "port" : splited_log[-2],
        "protocol" : splited_log[-1]
    })


# Now, only working with le list of dictionnaries list_dict_logs

# Count failed and accepted password
accepted_password = 0
failed_password = 0
failed_logs = []
ip_addresses_failed_password = []
hosts_failed_password = []
users_failed_password = []
protocols_failed_password = []

for log_dict in list_dict_logs :
    event = log_dict.get("event")
    if event == "Failed password":
        failed_password += 1
        failed_logs.append(log_dict)
        ip_addresses_failed_password.append(log_dict.get("ip"))
        hosts_failed_password.append(log_dict.get("host"))
        users_failed_password.append(log_dict.get("user"))
        protocols_failed_password.append(log_dict.get("protocol"))
        
    elif event == "Accepted password":
        accepted_password += 1

# use Counter to find the most used IP, user, host, protocol
count_ip_addresses = Counter(ip_addresses_failed_password)  
count_users = Counter(users_failed_password)
count_hosts = Counter(hosts_failed_password)
count_protocols = Counter(protocols_failed_password)

# display most common IP for all failed attempts
total_failed_attempts = 0
for ip, count in count_ip_addresses.most_common() :
    total_failed_attempts += count
    print(f"The IP address {ip} failed to login {count} times.")
print(f"Total failed attempts = {total_failed_attempts}.")

# display most common user for all failed attempts
for user, count in count_users.most_common() :
    print(f"The user {user} failed to login {count} times.")

# diplay most common host for all failed attempts
for host, count in count_hosts.most_common():
    print(f"The host {host} was targeted {count} times.")

# display most common protocol far all failed attempts
for protocol, count in count_protocols.most_common():
    print(f"The protocol {protocol} has been used for a failed login attempt {count} times.")

# display the timestamp of the first and the last failed occurence
print(f"The first failed occured at {failed_logs[0]["timestamp"]}.")
print(f"The last failed occured at {failed_logs[-1]["timestamp"]}.")

# calculate the time between these two timestamp
first_dt = datetime.strptime("2026 " + failed_logs[0]["timestamp"], "%Y %b %d %H:%M:%S")
last_dt = datetime.strptime("2026 " + failed_logs[-1]["timestamp"], "%Y %b %d %H:%M:%S")

# display the difference between the two datetime objects
print(f"{total_failed_attempts} failed attempts occured in (time) : {last_dt - first_dt}")