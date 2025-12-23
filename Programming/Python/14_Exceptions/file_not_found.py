# Write a program to generate FileNotFoundException
try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
    print(content)
except FileNotFoundError:
    print("FileNotFoundException occurred")