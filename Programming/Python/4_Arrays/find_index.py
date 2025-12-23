# Write a program to find the index of an array element

arr = [5, 10, 15, 20]
search = 15
index = 0
found = False

for value in arr:
    if value == search:
        print(index)
        found = True
        break
    index = index + 1

if found == False:
    print("Element not found")
