# Write a method to verify if the array contains two specified elements(12,23)

arr = [10, 12, 15, 23]
found_12 = False
found_23 = False

for value in arr:
    if value == 12:
        found_12 = True
    if value == 23:
        found_23 = True

if found_12 and found_23:
    print("Both elements found")
else:
    print("Elements not found")
