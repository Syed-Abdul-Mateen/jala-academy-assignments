# Write two methods with the same name and same number of parameters of same type

class Sample:
    def display(self, value):
        print("Second method overrides first:", value)

s = Sample()
s.display(100)
