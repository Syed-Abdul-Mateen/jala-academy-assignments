# Define a static variable and change within the instance

class Student:
    college = "ICFAI"

s1 = Student()
s1.college = "JALA"
print(s1.college)
print(Student.college)
