def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example usage
n = int(input("Enter a number: "))
print("Factorial of", n, "is", factorial(n))

