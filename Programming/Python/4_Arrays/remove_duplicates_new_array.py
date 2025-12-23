# Write a program to remove the duplicate elements and return the new array

arr = [1, 2, 2, 3, 4, 4]
new_array = []

for value in arr:
    if value not in new_array:
        new_array.append(value)

print(new_array)
