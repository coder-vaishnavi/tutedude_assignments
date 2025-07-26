student_marks = {
    "vaishnavi": 85,
    "Baban": 90,
    "Chetan": 78,
    "rana": 92
}

# Step 2: Input student name
name = input("Enter the student's name: ")

# Step 3 & 4: Check and print result
if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print("Student not found in the record.")
