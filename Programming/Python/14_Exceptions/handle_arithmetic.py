# Handle the Arithmetic exception using try-catch block
try:
    result = 10 / 0
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero")