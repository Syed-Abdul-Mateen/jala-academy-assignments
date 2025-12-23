# Define a static variable and change within the class

class Student:
    college = "ICFAI"

Student.college = "JALA"

s1 = Student()
print(s1.college)
print(Student.college)
