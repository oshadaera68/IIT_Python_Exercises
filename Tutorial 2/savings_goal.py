#Saving Goal Tracker

#User Inputs
target_saving_goal = float(input("Input the target saving goal: "))
current_saving_amount = float(input("Input the current saving amount: "))
monthly_saving_amount = float(input("Input the monthly saving amount: "))

#counting the goal
months_needed = (target_saving_goal - current_saving_amount) / monthly_saving_amount
print("It will Take", months_needed, "Months.")
