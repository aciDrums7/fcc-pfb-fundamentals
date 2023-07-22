""" Lamba Functions """
from functools import reduce

double = lambda num: num * 2

# multiply = lambda a, b : a * b

# print(multiply(3,7))


# 2 map()

numbers = [1, 2, 3, 4, 5, 6, 7]

# result = map(double, numbers)

# print(list(result))


# 3 filter()

# isOdd = lambda n : n % 2 != 0

# result = filter(isOdd, numbers)

# print(list(result))


# 4 reduce()
expenses = [("Dinner", 80), ("Car repair", 120)]

# sum = 0
# for expense in expenses:
#     sum += expense[1]

sum = reduce(lambda a, b: a[1] + b[1], expenses)

print(sum)
