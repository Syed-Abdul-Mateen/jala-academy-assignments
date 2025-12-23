# Write a program to find Armstrong number or not

number = 153
temp = number
total = 0

while temp > 0:
    digit = temp % 10
    total = total + (digit * digit * digit)
    temp = temp // 10

if total == number:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
