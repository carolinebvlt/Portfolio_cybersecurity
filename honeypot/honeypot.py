def save_attempt(ip, username, password):
    with open("logs.txt", "a") as file:
        file.write(f"{ip} | {username} | {password}\n")


save_attempt("127.0.0.1", "admin", "123456")