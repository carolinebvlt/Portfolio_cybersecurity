# Write and read a file in Python

with open("./generated_files/test.txt", "w") as file :
    myText = "Hello world !"
    file.write(myText)

with open("./generated_files/test.txt", "r") as file :
    text = file.read()
    print(text)