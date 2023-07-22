""" 2 Tuples -> immutable data structure """
names = ("Syd", "Roger")

print(names[0])  # Roger
names.index("Roger")
len(names)  # 2
print("Roger" in names)

#! TypeError, tuples are immutable
# print(names.sort())
print(sorted(names))

# 1 When you use += with a tuple, you are not modifying the existing tuple in place.
# 2 Instead, you are creating a new tuple that is the concatenation of the original tuple
# 3 and another iterable (like another tuple or a list).
# 4 This new tuple is assigned to the same variable, making it appear as if you modified
# 5 the original tuple, but you actually created a new one.

print(id(names))
names += ("Tina", "Quincy")
print(id(names))

#! TypeError, tuples are immutable
# names[0] = "prova"
