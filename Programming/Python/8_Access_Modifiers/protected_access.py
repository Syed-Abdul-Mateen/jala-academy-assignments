# Create a class with PROTECTED fields and methods and access them from same and different classes

class Base:
    def __init__(self):
        self._course = "Python"

    def _show_course(self):
        print(self._course)

class SamePackage:
    def access_protected(self):
        b = Base()
        print(b._course)
        b._show_course()

class Child(Base):
    def access_from_child(self):
        print(self._course)
        self._show_course()

obj1 = SamePackage()
obj1.access_protected()

obj2 = Child()
obj2.access_from_child()
