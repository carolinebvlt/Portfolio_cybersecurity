import os

# Function that scan a directory and return a list of files
def scanner(dir_to_analyze) :
    list_of_files = []
    for file in os.listdir(dir_to_analyze):
        path = os.path.join(dir_to_analyze, file)

        if os.path.isfile(path):
            list_of_files.append(path)
    
    return list_of_files
