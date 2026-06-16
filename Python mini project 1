student_name=input("Enter the name of the Student:\n")
number_of_subjects=int(input("Enter the number of subjects:\n"))
subjects_list=[]
marks_list=[]

for i in range(1,number_of_subjects+1):
    print(f"Enter the sub {i} details")
    subjects_list.append(input("Enter the Subject name:\n"))
    marks_list.append(int(input("Enter the marks in subject:\n")))

print("+-------------------------------------------+")
print("| QIS College of Engineering and Technology |")
print("+-------------------------------------------+")

print("Name of the student: ",student_name)

for j in range(len(subjects_list)):
    print(subjects_list[j],":",marks_list[j])

print("Total marks:",sum(marks_list))
print("Average marks:",sum(marks_list)/len(marks_list))
print("Minimum Score:",min(marks_list))
print("Maximum Score:",max(marks_list))

failed_marks=[]

for m in range(len(marks_list)):
    if marks_list[m] < 35:
        failed_marks.append(subjects_list[m])

if len(failed_marks) > 0:
    print("+-------------------+")
    print("|   Results: Fail   |")
    print("+-------------------+")
    print("Failed Subjects List:")

    for subject in failed_marks:
        print(subject)

else:
    print("+-------------------+")
    print("|   Results: Pass   |")
    print("+-------------------+")
