# Create a class with PUBLIC fields and methods and access them from same and different classes

class Student:
    name = "Mateen"

    def show_name(self):
        print(self.name)

class AnotherClass:
    def access_public(self):
        s = Student()
        print(s.name)
        s.show_name()

s1 = Student()
s1.show_name()

a = AnotherClass()
a.access_public()
