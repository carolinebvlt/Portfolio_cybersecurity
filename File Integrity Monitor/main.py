import os
import json
from scanner import scanner
from hasher import hasher
from storage import storage


# Select a directory to analyze  
dir_to_analyze = "SSH_log_analyzer"

# Check if there is a baseline file for that directory
json_name = f"baseline_{dir_to_analyze}.json"
base_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(base_dir, json_name)

# Call scanner function that returns the list of files
list_of_files = scanner(dir_to_analyze)

# Loop for each file to hash it, 
# then add it to a dictionnary that will be compared to the basline
file_hashes = {}
for file_to_analyze in list_of_files :
    file_hash = hasher(file_to_analyze)
    file_hashes[file_to_analyze] = file_hash


if os.path.exists(path):
    # check if the content of the baseline is the same than file_hashes
    with open(path, 'r') as file:
        baseline = json.load(file)
    if baseline == file_hashes :
        #if the content is the same, store the new baseline
        print("same hash")
        storage(file_hashes,dir_to_analyze)
    else :
        print("different hash")
        #find what has been modified
        for file_to_check, hash in file_hashes.items():
            if baseline[file_to_check] != hash :
                print(f"This file has been modified : {file_to_check}")
        # store new baseline
        storage(file_hashes,dir_to_analyze)

else :
    storage(file_hashes, dir_to_analyze)