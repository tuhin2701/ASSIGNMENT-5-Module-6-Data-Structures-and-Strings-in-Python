
student_marks={'John':85,'Stacy':54,'Mark': 74, 'Sameer':89, 'Aman':35,'Nitin':50}

student_name = input("Enter the student's name: ")

if student_name in student_marks:
    print(f"{student_name}'s marks: {student_marks[student_name]}")
else:
    print("Student not found.")