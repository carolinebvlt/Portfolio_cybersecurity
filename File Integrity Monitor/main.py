import os
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
    print(f'yes')
    # check if the content of the baseline is the same than file_hashes

else :
    print(f"no : {path}")
    storage(file_hashes, dir_to_analyze)