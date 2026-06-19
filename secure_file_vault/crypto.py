from cryptography.fernet import Fernet
import os


# generate a key 
def generate_key():
    key = Fernet.generate_key()

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    key_path = os.path.join(BASE_DIR, "key.key")

    with open(key_path, "wb") as key_file:
        key_file.write(key)

# Load a key
def load_key():

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    key_path = os.path.join(BASE_DIR, "key.key")

    with open(key_path, "rb") as key_file:
        return key_file.read()
    
# encrypt a file
def encrypt_file(file_path):
    key = load_key()
    f = Fernet(key)

    with open(file_path, "rb") as file:
        data = file.read()

    encrypted_data = f.encrypt(data)

    with open(file_path + ".enc", "wb") as file:
        file.write(encrypted_data)

# decrypt a file
def decrypt_file(file_path):
    key = load_key()
    f = Fernet(key)

    with open(file_path, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = f.decrypt(encrypted_data)

    output_path = file_path.replace(".enc", "")

    with open(output_path, "wb") as file:
        file.write(decrypted_data)