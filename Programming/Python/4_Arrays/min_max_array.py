# Write a function to find the minimum and maximum value of an array

def min_max(arr):
    minimum = arr[0]
    maximum = arr[0]

    for value in arr:
        if value < minimum:
            minimum = value
        if value > maximum:
            maximum = value

    print("Min:", minimum)
    print("Max:", maximum)

arr = [12, 5, 30, 7]
min_max(arr)
