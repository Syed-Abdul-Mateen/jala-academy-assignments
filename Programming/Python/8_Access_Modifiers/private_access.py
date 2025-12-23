# Create a class with PRIVATE fields, private method and access them in main method and sub class

class Parent:
    def __init__(self):
        self.__salary = 50000

    def __show_salary(self):
        print(self.__salary)

    def access_private(self):
        print(self.__salary)
        self.__show_salary()

class Child(Parent):
    def try_access(self):
        try:
            print(self.__salary)
        except:
            print("Cannot access private variable")

p = Parent()
p.access_private()

c = Child()
c.try_access()