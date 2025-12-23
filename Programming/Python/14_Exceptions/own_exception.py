# Write a program to create your own exception
class InvalidAgeException(Exception):
    pass

try:
    age = 15
    if age < 18:
        raise InvalidAgeException("Age must be 18 or above")
    print(f"Age: {age} is valid")
except InvalidAgeException as e:
    print(f"Custom exception caught: {e}")