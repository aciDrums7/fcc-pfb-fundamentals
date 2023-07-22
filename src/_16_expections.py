""" Exceptions"""

try:
    result = 2 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    result = 1

print(result)

# raise Exception("ORRORE!")

try:
    raise Exception("ORRORE!")
except Exception as error:
    print(error)


class DogNotFoundException(Exception):
    """Dog not found"""

    # ? Pass is utilized as placeholder, like 'Lorem ipsum...'
    pass


try:
    raise DogNotFoundException()
except DogNotFoundException:
    print("Dog not found!")


filename = "/Users/ciccio/test.txt"

# try:
#     file = open(filename, 'r')
#     content = file.read()
#     print(content)
# finally:
#     file.close()

# ? try/catch 'with' resources
with open(filename, "r") as file:
    content = file.read()
    print(content)
