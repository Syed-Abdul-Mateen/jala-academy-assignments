# Create objects for A, B and C and demonstrate method overriding and runtime polymorphism

from class_a import A
from class_b import B
from class_c import C

a = A()
b = B()
c = C()

a.method_one()
a.method_two()
a.show()
print(a.value)

b.method_three()
b.method_four()
b.show()
print(b.value)

c.method_five()
c.method_six()
c.show()
print(c.value)

ref = A()

ref = b
ref.show()
print(ref.value)

ref = c
ref.show()
print(ref.value)
