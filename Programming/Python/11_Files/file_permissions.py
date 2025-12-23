# Write a program to check whether a file is having read access and write access permissions

import os

file_name = "sample.txt"

print(os.access(file_name, os.R_OK))
print(os.access(file_name, os.W_OK))
