""" 3 Dictionaries """
dog = {"name": "Roger", "age": 8}
print(dog.get("name"))
print(dog.get("color"))

# ? Default value
print(dog.get("color", "brown"))
dog.update({"color": "green"})
print(dog.get("color", "brown"))

# Delete values
dog.pop("name")
print(dog)

dog.popitem()
print(dog)

print("age" in dog)

print(dog.keys())
print(list(dog.keys()))

print(list(dog.values()))

print(list(dog.items()))

print(len(dog))

dog["favorite food"] = "meat"
print(dog)

del dog["age"]
print(dog)
