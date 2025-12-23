# Write a program to palindrome or not

number = 121
temp = number
reverse = 0

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp = temp // 10

if reverse == number:
    print("Palindrome")
else:
    print("Not a Palindrome")
