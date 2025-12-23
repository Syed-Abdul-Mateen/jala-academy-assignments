# Write a function to insert an element at a specific position in the array

def insert_element(arr, position, element):
    new_array = []
    index = 0
    for value in arr:
        if index == position:
            new_array.append(element)
        new_array.append(value)
        index = index + 1
    print(new_array)

arr = [10, 20, 30]
insert_element(arr, 1, 15)
