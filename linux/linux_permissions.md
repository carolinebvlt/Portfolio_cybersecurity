# Permissions in Linux

## Project description
Here are the main command lines for managing permissions for files and folders in Linux
## Check file and directory details
`ls -l` to display details about permissions
`ls -la` to also deplay details about hidden files
## Describe the permissions string
`drwxrwxrwx` 
It starts with a `d` for a directory and with `-` for a file.
First three letters are permissions of the user.
Next three letters are permissions for the group.
Last three letters are permissions for the others.
`r` : read
`w` : write
`x` : execute
## Change file permissions
`chmod g+w,o-r file.txt`
This command line would add writing permission for the group and remove reading permission for the others.

## Change directory permissions
`chmod g+x directory/`
This command line would add permission for the group to access the directory
