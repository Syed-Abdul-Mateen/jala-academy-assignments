# Write two methods with the same name but different number of parameters of different data type and call the methods

class Display:
    def show(self, value1, value2=None):
        if value2 is None:
            print(value1)
        else:
            print(value1, value2)

d = Display()
d.show(10)
d.show("Age", 21)
