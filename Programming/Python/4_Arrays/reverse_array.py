# Write a function to reverse an array of integer values

def reverse_array(arr):
    reversed_array = []
    index = 0
    for value in arr:
        reversed_array.insert(0, value)
    print(reversed_array)

arr = [1, 2, 3, 4]
reverse_array(arr)
