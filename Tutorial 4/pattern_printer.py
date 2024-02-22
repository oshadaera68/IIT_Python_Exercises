number = int(input("Enter the number: "))
spaces = 0
stars = 0
for i in range(1, number + 1):
    print(" " * (number - i), end="")
    print("*" * (2*i - 1))
