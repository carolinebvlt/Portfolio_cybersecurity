import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("127.0.0.1", 5000))

server.listen(1)

print("Honeypot ON... waiting for a connexion...")

client, address = server.accept()

print("Connexion reçue !")
print("Adresse :", address)

client.close()
server.close()