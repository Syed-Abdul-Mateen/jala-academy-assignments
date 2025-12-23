# Write a program to read a file a just to a particular index using seek()

file = open("sample.txt", "r")
file.seek(9)
print(file.read())
file.close()
