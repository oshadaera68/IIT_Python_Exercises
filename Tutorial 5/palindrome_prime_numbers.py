for number in range(2, 1000):
    is_prime = True
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        is_palindromic = str(number) == str(number)[::-1]
        if is_palindromic:
            print(number)
