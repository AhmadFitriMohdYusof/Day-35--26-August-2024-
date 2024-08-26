def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = 4
result = fibonacci(n)
print(f"The {n}th Fibonacci number is: {result}")
