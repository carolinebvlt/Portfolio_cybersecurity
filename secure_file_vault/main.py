from crypto import generate_key, encrypt_file, decrypt_file
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def main():
        
    # Infinite loop so the program turns until the user exit (command 4)
    while True :

        print("=== SECURE FILE VAULT ===")
        print("1. Generate key")
        print("2. Encrypt file")
        print("3. Decrypt file")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            generate_key()
            print("Key generated successfully.")

        elif choice == "2":
            file_path = input("Enter file to encrypt: ")
            real_file_path = os.path.join(BASE_DIR, file_path)
            encrypt_file(real_file_path)
            print("File encrypted.")

        elif choice == "3":
            file_path = input("Enter file to decrypt: ")
            real_file_path = os.path.join(BASE_DIR ,file_path)
            decrypt_file(real_file_path)
            print("File decrypted.")

        elif choice == "4":
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()