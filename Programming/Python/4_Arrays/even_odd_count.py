# Write a method to find number of even number and odd numbers in an array

arr = [1, 2, 3, 4, 5]
even = 0
odd = 0

for value in arr:
    if value % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

print("Even:", even)
print("Odd:", odd)
