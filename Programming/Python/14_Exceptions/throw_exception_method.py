# Write a method which throws exception, Call that method in main class without try block
def divide_numbers(a, b):
    return a / b

# This will raise an exception when called
result = divide_numbers(10, 0)
print(result)