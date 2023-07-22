""" Objects """

#! Everything in Python is an object, even functions and primitives

# 0 primitives -> immutable objects
age = 8

print(age.real)
print(age.imag)
print(age.bit_length())


# 1 Lists -> mutable objects

items = [1, 2]

items.append(3)
items.pop()
print(id(items))
