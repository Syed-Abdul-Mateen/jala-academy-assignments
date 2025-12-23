# Write a class with a default constructor, one argument constructor and two argument constructors

class Student:
    def __init__(self, name=None, age=None):
        if name is None and age is None:
            print("Default Constructor")
        elif age is None:
            print("One Argument Constructor:", name)
        else:
            print("Two Argument Constructor:", name, age)

Student()
Student("Mateen")
Student("Mateen", 21)
