# Write a program to read text file

file = open("sample.txt", "r")
content = file.read()
print(content)
file.close()
