""" 0 From Variables to Control Statements """
NAME = "20"

# print(type(name) == str)
print(isinstance(NAME, str))

# casting
age = float(NAME)

print(isinstance(age, float))

# is operator
print(NAME is age)

# in operator
print(NAME in [13, 7, "20"])


def is_adult(_age):
    """return true if > 18"""
    return _age > 18


print(is_adult(17))

print(
    """Beau is

39

years old
"""
)

print("Lorem Ipsum".title())

# ? character escaping
print('Be"au')

print("Beau"[1])
print("Beau"[0:3])
print("Beau"[2:])
