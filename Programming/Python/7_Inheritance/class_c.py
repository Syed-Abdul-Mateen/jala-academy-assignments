# C is a sub class of B

from class_b import B

class C(B):
    value = "Value from C"

    def method_five(self):
        print("Method five from C")

    def method_six(self):
        print("Method six from C")

    def show(self):
        print("Show method from C")
