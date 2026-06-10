# Create a function to update a .txt file with allowed IP addresses 
# by removing a given list of IP addresses 

def remove_addresses(allowed_addresses_file_path, to_remove_list) :

    # Open the allowed addresses file, read it, and parse it into a list
    with open(allowed_addresses_file_path, "r") as file :
        allowed_addresses_text = file.read()
        allowed_addresses_list = allowed_addresses_text.split()

    # Remove the IP from the list with a for loop
    for ip in allowed_addresses_list :
        if ip in to_remove_list :
            allowed_addresses_list.remove(ip)

    # Rewrite the file with the updated list of allowed addresses in the .txt format
    updated_allowed_addresses_txt = " ".join(allowed_addresses_list)
    with open(allowed_addresses_file_path, "w") as file :
        file.write(updated_allowed_addresses_txt)

allowed_addresses_file_path = "./generated_files/allowed_ip_addresses.txt"
to_remove_list = ["192.168.25.60", "192.168.140.81", "192.168.203.198"]

# Call the function
remove_addresses(allowed_addresses_file_path, to_remove_list)