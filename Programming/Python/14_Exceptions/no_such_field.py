# Write a program to generate NoSuchFieldException
class Person:
    def __init__(self):
        self.name = "John"
        self.age = 25

try:
    p = Person()
    # Try to access non-existent attribute
    value = p.address  # This will raise AttributeError
    print(value)
except AttributeError:
    print("NoSuchFieldException equivalent: Attribute not found")