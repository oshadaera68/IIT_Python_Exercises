# Fibonacci Sequence print using the list
def fib_sequence(n):
    fib_sequence = [0, 1]
    for i in range(n):
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)

    return fib_sequence


# Testing Purpose
result = fib_sequence(10)
print(result)
