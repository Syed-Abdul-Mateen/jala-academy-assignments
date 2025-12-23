# Write a program to throw exception with your own message
try:
    age = -5
    if age < 0:
        raise ValueError("Age cannot be negative")
    print(f"Age: {age}")
except ValueError as e:
    print(f"Error: {e}")