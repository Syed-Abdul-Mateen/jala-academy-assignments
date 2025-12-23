# Write a program to find the prime or not

number = 7
count = 0
i = 1

while i <= number:
    if number % i == 0:
        count = count + 1
    i = i + 1

if count == 2:
    print("Prime Number")
else:
    print("Not a Prime Number")
