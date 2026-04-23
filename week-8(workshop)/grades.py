students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 90
}
with open("grades.txt", "w") as file:
    for name, grade in students.items():
        file.write(f"{name},{grade}\n")

total_grade = 0
count = 0
print("--- Student Data ---")
with open("grades.txt", "r") as file:
    for line in file:
        name, grade = line.strip().split(",")
        grade = int(grade)
        print(f"Student: {name} | Grade: {grade}")
        
        total_grade += grade
        count += 1
if count > 0:
    average = total_grade / count
    print("--------------------")
    print(f"Average Grade: {average:.2f}")