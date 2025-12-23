# Create a Dictionary with at least 5 key value pairs of the Student ID and Name

students = {
    101: "Ayaan",
    102: "Rahul",
    103: "Neha",
    104: "Sahil",
    105: "Priya"
}

print(students)


# Adding the values in dictionary

students[106] = "Kiran"
print(students)


# Updating the values in dictionary

students[102] = "Rohit"
print(students)


# Accessing the value in dictionary

print(students[103])


# Create a nested loop dictionary

student_details = {
    1: {"id": 101, "name": "Ayaan"},
    2: {"id": 102, "name": "Rohit"},
    3: {"id": 103, "name": "Neha"}
}

print(student_details)


# Access the values of nested loop dictionary

print(student_details[1]["name"])
print(student_details[2]["id"])


# Print the keys present in a particular dictionary

for key in students:
    print(key)


# Delete a value from a dictionary

del students[104]
print(students)
