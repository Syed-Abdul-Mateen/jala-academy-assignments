# Write a program to find the common values between two arrays

arr1 = [1, 2, 3, 4]
arr2 = [3, 4, 5, 6]
common = []

for a in arr1:
    for b in arr2:
        if a == b:
            common.append(a)

print(common)
