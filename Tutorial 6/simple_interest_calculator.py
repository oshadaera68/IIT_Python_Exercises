# Simple Interest Calculator
def calculate_simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest


# Testing
result = calculate_simple_interest(10000, 12, 5)
print(result)
