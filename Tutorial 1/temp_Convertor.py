#Temp Convertor
print("Temp Conversion Program")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
choice = int(input("Select a Choice: "))
fahrenheit = 0
celsius = 0

if choice == 1:
    celsius = float(input("Enter the Number: "))
    fahrenheit = (celsius * 9/5) + 32
    print("Fahrenheit Value is: ", fahrenheit)
elif choice == 2:
    fahrenheit = float(input("Enter the number: "))
    celsius = (fahrenheit - 32) * 5/9
    print("Celsius Value is: ", celsius)
else:
    print("Invalid Value!! Please type a valid value")
