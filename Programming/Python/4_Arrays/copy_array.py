# Write a function to copy an array to another array

def copy_array(arr):
    new_array = []
    for value in arr:
        new_array.append(value)
    print(new_array)

arr = [5, 10, 15]
copy_array(arr)
