# calculate the power of number without ** operator
def expo_calc(base, exponent):
    result = 1

    if exponent < 0:
        base = 1 / base
        exponent = -exponent

    for _ in range(exponent):
        result *= base

    return result


# Testing
result = expo_calc(2, 4)
print(result)
