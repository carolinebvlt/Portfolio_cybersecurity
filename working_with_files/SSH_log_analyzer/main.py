import os
import re
from collections import Counter

# Open the file named ssh_logs.txt that's in the same directory than this script
base_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(base_dir, "ssh_logs.txt")

with open(path, "r") as file:
    logs = file.readlines()

# Init login attemps counters
successful_login_attemps = 0
failed_login_attempts = 0
ip_addresses = []
ip_addresses_failed_login_attempts = []

for log in logs :

    # find the ip address and add them in ip_addresses list (to count later which ones are the most active)
    user_and_ip = re.search(r"for (\w+) from (\d+\.\d+\.\d+\.\d+)", log)
    if user_and_ip:
        ip_addresses.append(user_and_ip.group(2))

    # Count password events (Accepted or Failed)
    if "Accepted password" in log :
        successful_login_attemps += 1
    elif "Failed password" in log :
        failed_login_attempts += 1
        ip_addresses_failed_login_attempts.append(user_and_ip.group(2))

count_ip_addresses = Counter(ip_addresses)
print(count_ip_addresses.most_common())
print("_______________________________")
count_ip_addresses_failed_login_attempts = Counter(ip_addresses_failed_login_attempts)
print(count_ip_addresses.most_common())
    