print("STUDENT PROGRESS TRACKER")
print("----------------------------")

sname = input("Enter the Student Name: ")
Branch = input("Enter the Branch: ")
Year = int(input("Enter the Year (1/2/3/4): "))
sem = int(input("Enter the Semester (1/2): "))
Rollno = input("Enter the Roll No: ")

entered_marks1 = int(input("Enter the Subject-1 Marks: "))
entered_marks2 = int(input("Enter the Subject-2 Marks: "))
entered_marks3 = int(input("Enter the Subject-3 Marks: "))
entered_marks4 = int(input("Enter the Subject-4 Marks: "))
entered_marks5 = int(input("Enter the Subject-5 Marks: "))

# Calculate Total, Average
total = entered_marks1 + entered_marks2 + entered_marks3 + entered_marks4 + entered_marks5
average = total / 5

# Grade Calculation
if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"
print("\n===== STUDENT PROGRESS REPORT =====")
print(f"Name           : {sname}")
print(f"Branch         : {Branch}")
print(f"Year           : {Year}")
print(f"Semester       : {sem}")
print(f"Roll Number    : {Rollno}")
print("--------------------------------------")
print("Marks Obtained:")
print(f"Subject 1      : {entered_marks1}")
print(f"Subject 2      : {entered_marks2}")
print(f"Subject 3      : {entered_marks3}")
print(f"Subject 4      : {entered_marks4}")
print(f"Subject 5      : {entered_marks5}")
print("--------------------------------------")
print(f"Total Marks    : {total}/500")
print(f"Average        : {average:.2f}")
print(f"Grade          : {grade}")
print("======================================")
