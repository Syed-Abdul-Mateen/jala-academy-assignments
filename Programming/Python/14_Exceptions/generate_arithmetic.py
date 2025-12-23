# Write a program to generate Arithmetic Exception
def calculate():
    return 100 / 0

try:
    result = calculate()
    print(result)
except ZeroDivisionError as e:
    print(f"Arithmetic Exception: {e}")