# generate a marksheet using if else and elif statement

student_percentage: int = int(input("Enter student percentage"))
if student_percentage >= 90:
    print("you got A+ grade")
elif student_percentage >= 80:
    print("you got A grade")
elif student_percentage >= 70:
    print("you got B grade")
elif student_percentage >= 60:
    print("you got C grade")
elif student_percentage >= 50:
    print("you got D grade")
elif student_percentage >= 40:
    print("you got E grade")
elif student_percentage >= 30:
    print("you got F grade") 
else:
    print("you are fail in exam")