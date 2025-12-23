# Write a program to read a file stream supports random access

file = open("sample.txt", "r")
file.seek(0)
print(file.read())
file.close()
