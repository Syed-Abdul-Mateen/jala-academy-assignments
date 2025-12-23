# B is a sub class of A

from class_a import A

class B(A):
    value = "Value from B"

    def method_three(self):
        print("Method three from B")

    def method_four(self):
        print("Method four from B")

    def show(self):
        print("Show method from B")
