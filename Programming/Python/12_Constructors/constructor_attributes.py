# Write a program which illustrates the concept of attributes of a constructor

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

e = Employee("Rahul", 50000)
print(e.name)
print(e.salary)
