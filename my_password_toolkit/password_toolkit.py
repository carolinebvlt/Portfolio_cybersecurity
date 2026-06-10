from password_checker import check_password_strength

# Ask user which command to exec : 
# 1. check a password strength
# 2. generate a strong password
command_to_exec = 0
while command_to_exec != 1 and command_to_exec != 2 :
    command_to_exec = int(input("Enter '1' to check the strength of a password, or '2' to generate a strong password "))

# 1. check a password strength
if command_to_exec == 1 :
    password_to_check = ""
    while len(password_to_check) < 1 :
        password_to_check = input("Enter a password to check its strength : ")
    password_score, password_strength_level = check_password_strength(password_to_check)
    print(f"The strength level of this password is '{password_strength_level}' (score : {password_score})")