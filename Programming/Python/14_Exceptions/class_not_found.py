# Write a program to generate ClassNotFoundException
try:
    # In Python, we use __import__ or importlib for dynamic imports
    module_name = "non_existent_module"
    __import__(module_name)
except ModuleNotFoundError:
    print("ClassNotFoundException equivalent: Module not found")