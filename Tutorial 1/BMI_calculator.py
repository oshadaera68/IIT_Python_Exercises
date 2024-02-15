weight = float(input("Enter Your Weight: "))
height = float(input("Enter Your Height: "))
bmi = weight / (height ** 2)
if bmi < 18.5:
    print("Underweight")
elif bmi >= 18.5 and bmi < 25:
    print("Normal weight")
elif bmi >= 25 and bmi < 30:
    print("Overweight")
else:
    print("Obese")
