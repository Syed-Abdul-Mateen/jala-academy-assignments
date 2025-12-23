# Call the constructors(both default and argument constructors) of super class from a child class

class Parent:
    def __init__(self, value=None):
        if value is None:
            print("Parent Default Constructor")
        else:
            print("Parent Argument Constructor:", value)

class Child(Parent):
    def __init__(self, value=None):
        super().__init__(value)
        print("Child Constructor")

Child()
Child(100)
