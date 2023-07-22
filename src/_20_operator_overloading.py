""" Operator Overloading """


class Dog:
    """Dog class"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # ? Similar to Java Comparator/Comparable interfaces implementation
    # 1 gt -> greater than
    def __gt__(self, other):
        return self.age > other.age


roger = Dog("Roger", 6)
syd = Dog("Syd", 7)

# ? Operator overloading -> having defined the __gt__ method, now I can
# ? compare two dog instances using the greater operator
print(roger < syd)
