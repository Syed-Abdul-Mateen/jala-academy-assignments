# Write a function to test if array contains a specific value

def contains_value(arr, key):
    for value in arr:
        if value == key:
            print("Value found")
            return
    print("Value not found")

arr = [2, 4, 6, 8]
contains_value(arr, 6)
