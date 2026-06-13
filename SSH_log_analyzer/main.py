import os
import re
from collections import Counter
from datetime import datetime

# Open the file named ssh_logs.txt that's in the same directory than this script
base_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(base_dir, "ssh_logs.txt")

with open(path, "r") as file:
    logs = file.readlines()

# STEP 1 : PARSING ---------------------------------------------------------

# Init a list of dictionnaries (one dict for each log)
list_dict_logs = []


for log in logs :

    # For each log, create a dictionnary with :
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

# STEP 2 : COUNTING ----------------------------------------------------

# Now, only working with the list of dictionnaries list_dict_logs

# Count failed and accepted password
# Init some lists needed for further analyze
accepted_password = 0
failed_password = 0
failed_logs = []
ip_addresses_failed_password = []
ip_addresses_accepted_password = []
hosts_failed_password = []
users_failed_password = []
protocols_failed_password = []
dict_ip_timestamps = {}

# For each log
for log_dict in list_dict_logs :
    event = log_dict.get("event")
    # if the event is "Failed password" :
    # add it to lists to count later and find suspicious behavior
    if event == "Failed password":
        failed_password += 1
        failed_logs.append(log_dict)
        ip_addresses_failed_password.append(log_dict.get("ip"))
        hosts_failed_password.append(log_dict.get("host"))
        users_failed_password.append(log_dict.get("user"))
        protocols_failed_password.append(log_dict.get("protocol"))

        # create new dictionnary with ip as keys and list of timestamps as value
        # to calculate the duration bewteen first and last attempt of each IP address
        if log_dict.get("ip") not in dict_ip_timestamps :
            dict_ip_timestamps[log_dict.get("ip")] = []
        dict_ip_timestamps[log_dict.get("ip")].append(log_dict.get("timestamp"))

    elif event == "Accepted password":
        accepted_password += 1
        # add to the list ip_addresses_accepted_password to check later if a suspicious IP succeeded to login
        ip_addresses_accepted_password.append(log_dict.get("ip"))

# use Counter to find the most used IP, user, host, protocol
count_ip_addresses = Counter(ip_addresses_failed_password)  
count_users = Counter(users_failed_password)
count_hosts = Counter(hosts_failed_password)
count_protocols = Counter(protocols_failed_password)

# STEP 3 : DISPLAY ---------------------------------------------------

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

# display most common protocol for all failed attempts
for protocol, count in count_protocols.most_common():
    print(f"The protocol {protocol} has been used for a failed login attempt {count} times.")

# display the timestamp of the first and the last failed occurence
print(f"The first failed occured at {failed_logs[0]['timestamp']}.")
print(f"The last failed occured at {failed_logs[-1]['timestamp']}.")

# calculate the time between these two timestamp
first_dt = datetime.strptime("2026 " + failed_logs[0]['timestamp'], "%Y %b %d %H:%M:%S")
last_dt = datetime.strptime("2026 " + failed_logs[-1]['timestamp'], "%Y %b %d %H:%M:%S")

# display the difference between the two timestamps
duration = int(last_dt.timestamp()) - int(first_dt.timestamp())
print(f"{total_failed_attempts} failed attempts occured in (time) : {duration} seconds, or {duration/60} minutes")

# STEP 4 : ANALYZING / ALERT -------------------------------------------------
print("--------------------------------")

# ALERT if more than 10 failed attempts for ips and users
for ip, count in count_ip_addresses.most_common() :
    if count >= 5:
        print(f"ALERT : suspicious activity. {count} failed attempts for the IP {ip}")
        print(f"First attempt at : {dict_ip_timestamps.get(ip)[0]}")
        print(f"Last attempt at : {dict_ip_timestamps.get(ip)[-1]}")
        
        # convert to calculate the diff bewteen the two timestamps (first and last attempt)
        first_dt = datetime.strptime("2026 " + dict_ip_timestamps.get(ip)[0], "%Y %b %d %H:%M:%S")
        last_dt = datetime.strptime("2026 " + dict_ip_timestamps.get(ip)[-1], "%Y %b %d %H:%M:%S")
        duration = int(last_dt.timestamp()) - int(first_dt.timestamp())
        print(f"Duration between first and last attempt : {duration} seconds, or {duration/60} minutes")

        # check if the ip succeeded login
        if ip in ip_addresses_accepted_password :
            print(f"ALERT !!! The suspicious IP {ip} succeeded login")
        else :
            print(f"The suspicious IP {ip} didn't succeeded login")

for user, count in count_users.most_common():
    if count >= 10:
        print(f"ALERT : suspicious activity. {count} failed attempts for the user {user}")

