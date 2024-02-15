income = float(input("Enter Your Income: "))
tax_owed = 0
if income > 0:
    if income <= 12500:
        tax_owed = 0
    elif income <= 50000:
        tax_owed = (income - 12500) * 0.2
    elif income <= 150000:
        tax_owed = 7500 + (income - 50000) * 0.4
    else:
        tax_owed = 47500 + (income - 150000) * 0.45
else:
    print("You Entered Negative Number. Please Try again.")

net_income = income - tax_owed
print(f"Tax owed: £{tax_owed}")
print(f"Net Income(After Tax Deductions): £{net_income}")    
