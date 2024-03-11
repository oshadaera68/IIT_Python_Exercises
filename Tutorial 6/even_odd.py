# Finding the even or odd number using bitwise AND operator
def even_or_odd(number):
    return (number & 1) == 0


# Test the function
num = 5
if even_or_odd(num):
    print(num, "is even")
else:
    print(num, "is odd")
