# Write a program with multiple catch blocks
try:
    num = int("abc")  # This will cause ValueError
    result = 10 / 0   # This would cause ZeroDivisionError
except ValueError:
    print("Invalid number format")
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception as e:
    print(f"Other error: {e}")