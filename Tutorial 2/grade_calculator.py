sub1_marks = float(input("Enter the Subject 1 Marks: "))
sub2_marks = float(input("Enter the Subject 2 Marks: "))
sub3_marks = float(input("Enter the Subject 3 Marks: "))
sub4_marks = float(input("Enter the Subject 4 Marks: "))
sub5_marks = float(input("Enter the Subject 5 Marks: "))

sum_marks = sub1_marks + sub2_marks + sub3_marks + sub4_marks + sub5_marks
average = sum_marks / 5

print("Total Marks: ", sum_marks)
print("Your Average: ", average)

if average >= 75:
   print("Your Grade is A")
elif average >= 65:
    print("Your Grade is B")
elif average >= 50:
    print("Your Grade is C")
elif average >= 35:
    print("Your Grade is S")
else:
    print("Your Grade is F")
