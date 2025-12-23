# Write a function to find the duplicate values of an array

def find_duplicates(arr):
    duplicates = []
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j] and arr[i] not in duplicates:
                duplicates.append(arr[i])
    print(duplicates)

arr = [1, 2, 3, 2, 4, 3]
find_duplicates(arr)
