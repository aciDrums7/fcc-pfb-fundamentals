""" Loops """

condition = True
while condition:
    print("The condition is true")
    condition = False

count = 0
while count < 10:
    print("The condition is True")
    count += 1

print("After the loop")


items = [1, 2, 3, 4]
for item in items:
    print(item)


for item in range(7):
    print(item)


items = ["Beau", "Syd", "Quincy"]
# ? enumerate returns the item and its index
for index, item in enumerate(items):
    print(index, item)


# 1 Break and continue
items = [1, 2, 3, 4]
for item in items:
    if item == 3:
        # continue
        break
    print(item)
