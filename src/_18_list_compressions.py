""" List Compressions """

numbers = [1, 2, 3, 4, 5, 6, 7]

# 1 Manual way
# numbers_power_2 = []
# for n in numbers:
#     numbers_power_2.append(n**2)

# 2 Lambda way
# numbers_power_2 = list(map(lambda n: n**2, numbers))

# 3 List compression way
numbers_power_2 = [n**2 for n in numbers]

print(numbers_power_2)
