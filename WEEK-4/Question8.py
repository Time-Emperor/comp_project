name = input("Enter the student's name: ")
n_subjects = int(input("How many subjects? "))
marks = []

for i in range(n_subjects):
    mark = float(input(f"Enter mark for subject {i+1}: "))
    marks.append(mark)

highest = max(marks)
lowest = min(marks)
average = sum(marks) / len(marks)

if average >= 70:
    grade = "A"
elif average >= 60:
    grade = "B"
elif average >= 50:
    grade = "C"
elif average >= 40:
    grade = "D"
else:
    grade = "F"

print(f"\nStudent: {name}")
print(f"Highest Mark: {highest}")
print(f"Lowest Mark: {lowest}")
print(f"Average Mark: {average:.2f}")
print(f"Grade Obtained: {grade}")