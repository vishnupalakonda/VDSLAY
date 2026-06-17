def calculate_result(marks):
    total = sum(marks)
    average = round(total / len(marks), 2)
    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"
    return total, average, grade
print("--- Enter Student Details ---")
name = input("Enter student name: ")
age = int(input("Enter age: "))
marks = []
for i in range(1, 4):
    mark = float(input(f"Enter marks for Subject {i}: "))
    marks.append(mark)
student = {
    "name": name,
    "age": age,
    "marks": marks
}
total_marks, average_marks, final_grade = calculate_result(student["marks"])
print("\n" + "="*30)
print("        STUDENT REPORT        ")
print("="*30)
print(f"Student Name: {student['name']}")
print(f"Age: {student['age']}\n")
for index, mark in enumerate(student["marks"], start=1):
    print(f"Subject {index}: {mark}")
print("-" * 30)
print(f"Total: {total_marks}")
print(f"Average: {average_marks}")
print(f"Grade: {final_grade}")
print("="*30)
