# Write a function to get the difference of largest and smallest value

def difference(arr):
    min_val = arr[0]
    max_val = arr[0]

    for value in arr:
        if value < min_val:
            min_val = value
        if value > max_val:
            max_val = value

    print(max_val - min_val)

arr = [5, 20, 10]
difference(arr)
