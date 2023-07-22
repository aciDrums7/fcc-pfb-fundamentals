""" 1 Lists """
items = ["Roger", "Bou", "Bob", "Quincy"]

itemscopy = items[:]
items.sort(key=str.lower)

print(itemscopy)
print(items)

print(sorted(items, key=str.lower))
