# Write a program to generate IOException
try:
    # Try to write to a read-only file (simulated)
    file = open("read_only.txt", "w")
    # If file doesn't exist, we'll create it, but simulate IOError
    raise IOError("Disk is full or write protected")
except IOError as e:
    print(f"IOException occurred: {e}")