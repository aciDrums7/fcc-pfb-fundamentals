""" Polymorphism """


class Animal:
    """Animal class"""

    def eat(self):
        """eating animal's food"""
        print("Eating animal food")


class Dog(Animal):
    """Dog class"""

    def eat(self):
        print("Eating dog food")


class Cat(Animal):
    """Cat class"""

    def eat(self):
        print("Eating cat food")


dog = Dog()
cat = Cat()

dog.eat()
cat.eat()
