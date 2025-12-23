# Write a method to find the second largest number in an array

arr = [10, 5, 20, 15]

largest = arr[0]
second = arr[0]

for value in arr:
    if value > largest:
        second = largest
        largest = value
    elif value > second and value != largest:
        second = value

print(second)
