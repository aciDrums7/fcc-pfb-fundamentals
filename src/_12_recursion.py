""" Recursion """


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


print(factorial(1))
print(factorial(2))
print(factorial(3))
print(factorial(4))
print(factorial(5))
print(factorial(6))
print(factorial(7))
