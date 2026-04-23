n = int(input("Enter the number of students: "))
student_data = {}
for i in range(n):
    name = input(f"Enter name for student {i+1}: ")
    marks = float(input(f"Enter marks for {name}: "))
    student_data[name] = marks
print("\n--- Student Records ---")
for name, marks in student_data.items():
    print(f"Student: {name} | Marks: {marks}")