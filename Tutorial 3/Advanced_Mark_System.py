coursework_marks = int(input("Enter Coursework marks: "))
mid_exam_marks = int(input("Enter Mid term exam marks: "))
final_exam_marks = float(input("Enter the final exam score: "))

weighted_coursework = coursework_score * 0.4
weighted_midterm = midterm_score * 0.25
weighted_final_exam = final_exam_score * 0.35

final_grade = weighted_coursework + weighted_midterm + weighted_final_exam
if final_grade >= 70:
    letter_grade = 'A'
elif 50 <= final_grade < 70:
    letter_grade = 'B'
elif 40 <= final_grade < 50:
    letter_grade = 'C'
else:
    letter_grade = 'F'

print("Final Grade:", final_grade)
print("Letter Grade:", letter_grade)
