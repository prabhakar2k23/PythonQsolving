num = int(input("Enter a number to calculate its factorial: "))

def factorial(n):
    if n < 0:
        return "Factorial does not exist for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

print(f"The factorial of {num} is {factorial(num)}")
