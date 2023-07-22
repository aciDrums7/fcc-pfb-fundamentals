""" Classes """


class Animal:
    def walk(self):
        print("Walking...")


# * Inheritance
class Dog(Animal):
    # ? self points to current class instance
    # ? and must be specified to define class methods
    #! CONSTRUCTOR
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("woof woof MADAFACKA")


roger = Dog("Lola", 9)

print(type(roger))
print(roger.name)
print(roger.age)
roger.bark()
roger.walk()
