# Write a function to remove a specific element from an array

def remove_element(arr, key):
    new_array = []
    for value in arr:
        if value != key:
            new_array.append(value)
    print(new_array)

arr = [1, 2, 3, 2, 4]
remove_element(arr, 2)
