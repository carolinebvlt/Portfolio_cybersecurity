# File Integrity Monitor

The idea of this project is to create a tool able to detect if files have been modified, deleted or added.

In this project, im gonna try to work properly with separeted files for each function :
- main.py
Takes a directory as argument. If a baseline exists, it's compared to a new scan+hash+store operation. If not, the baseline is created.
- scanner.py
Scan all files in a directory and return a list of files
- hasher.py
Hash a file and return the hash
- storage.py
Store the baseline in a json file
- baseline.json
- report.py