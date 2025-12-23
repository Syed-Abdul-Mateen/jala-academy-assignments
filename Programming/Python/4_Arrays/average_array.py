# Write a function to calculate the average value of an array of integers

def average_array(numbers):
    total = 0
    count = 0
    for value in numbers:
        total = total + value
        count = count + 1
    print(total / count)

arr = [10, 20, 30, 40]
average_array(arr)
