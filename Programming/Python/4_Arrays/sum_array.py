# Write a function to add integer values of an array

def add_array(numbers):
    total = 0
    for value in numbers:
        total = total + value
    print(total)

arr = [10, 20, 30, 40]
add_array(arr)
