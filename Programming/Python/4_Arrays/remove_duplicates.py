# Write a method to remove duplicate elements from an array

def remove_duplicates(arr):
    result = []
    for value in arr:
        if value not in result:
            result.append(value)
    print(result)

arr = [1, 2, 2, 3, 4, 4]
remove_duplicates(arr)
