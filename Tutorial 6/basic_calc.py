# A basic calculator using function
def calculator(number1, number2, symbol):
    if symbol == "+":
        return number1 + number2
    elif symbol == "-":
        return number1 - number2
    elif symbol == "*":
        return number1 * number2
    elif symbol == "/":
        if number2 == 0:
            return "Zero Not Allowed!!"
        else:
            return number1 / number2
    else:
        return "Selected a Invalid Operation. Please Try again!!"


# Testing Purposes
result = calculator(1, 2, "+")
print(result)

result = calculator(1, 2, "-")
print(result)

result = calculator(1, 2, "*")
print(result)

result = calculator(2, 2, "/")
print(result)