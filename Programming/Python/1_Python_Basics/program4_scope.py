# Define the local and Global variables with the same name and print both variables and understand the scope of the variables

marks = 90

def result():
    marks = 75
    print(marks)

result()
print(marks)
