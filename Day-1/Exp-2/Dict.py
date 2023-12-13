# Create a dictionary that maps the names of students to their respective marks in an exam.
# Perform the following operation.
Student = {"Shankar": 98, "Biswajit": 87, "Prince": 63}
print("Student List: ", Student)

# Add a new student and their marks to the dictionary.
Student.update({"Aman": 75})
print("Updated Student List: ", Student)

# Calculate the average marks of all students.
print("Average marks: ", sum(Student.values()) / len(Student.values()))

# Find the student with the highest marks.
print("Highest marks: ", max(Student.items(), key=lambda x: x[1]))

# Sort the dictionary by student names in alphabetical order.
Sorted_Dict = sorted(Student)
print("Sorted Dictionary: ", Sorted_Dict)
