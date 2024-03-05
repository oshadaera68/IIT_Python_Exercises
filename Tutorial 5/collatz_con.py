starting_number = int(input("Enter a starting number: "))

while starting_number != 1:
    print(starting_number, end=" ")
    if starting_number % 2 == 0:
        starting_number //= 2
    else:
        starting_number = starting_number * 3 + 1

print(starting_number)
