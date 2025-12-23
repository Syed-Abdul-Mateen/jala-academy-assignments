# Write two methods with the same name but different number of parameters of same type and call the methods

class Calculator:
    def add(self, a, b, c=None):
        if c is None:
            print(a + b)
        else:
            print(a + b + c)

obj = Calculator()
obj.add(10, 20)
obj.add(10, 20, 30)
