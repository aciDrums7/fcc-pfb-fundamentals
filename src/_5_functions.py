""" Functions """


def hello():
    print("Hello!")


hello()
hello()
hello()


def hello2(name):
    print(f"Hello {name}!")


hello2("Ciccio")


# 2 Nested functions


def talk(phrase):
    def say(word):
        print(word)

    words = phrase.split(" ")
    for word in words:
        say(word)


talk("I'm going to buy the milk")


def count():
    count = 0

    def increment():
        #! UnboundLocalError: cannot access local variable 'count' where it is not associated with a value
        nonlocal count
        count += 1
        print(count)

    increment()


count()


# 3 Closures -> special way to do a function


def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    # ? Returning the function itself!
    return increment


increment = counter()

print(increment())  # 1
print(increment())  # 2
print(increment())  # 3
