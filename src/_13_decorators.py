""" Decorators """


def logtime(func):
    def wrapper(*args, **kwargs):
        print("before")
        val = func(*args, **kwargs)
        print("after")
        return val

    return wrapper


@logtime
def my_print(string):
    print(string)


@logtime
def mul(a, b):
    return a * b


my_print("Who are you to wave your finger!?")
print(mul(3, 7))
