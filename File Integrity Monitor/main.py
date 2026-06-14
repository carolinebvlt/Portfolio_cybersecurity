
from scanner import scanner
from hasher import hasher
from storage import storage

# Select a directory to analyze and call scanner function that returns the list of files
dir_to_analyze = "SSH_log_analyzer"
list_of_files = scanner(dir_to_analyze)

# Loop for each file to hash it, 
# then add it to a dictionnary that will be stored in JSON
file_hashes = {}
for file_to_analyze in list_of_files :
    file_hash = hasher(file_to_analyze)
    file_hashes[file_to_analyze] = file_hash
storage(file_hashes, dir_to_analyze)