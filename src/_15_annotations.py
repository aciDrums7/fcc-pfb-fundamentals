""" Annotations """


# ? Annotations in Python -> type definition
def increment(_n: int) -> int:
    """Returns n + 1"""
    return _n + 1


value: int = increment(6)

print(value)
