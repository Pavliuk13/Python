from sys import argv
from functools import reduce
from operator import add, sub, mul, truediv


def custom_calculate(user_input):
    try:
        elements = user_input[2:]
        operation = user_input[1]
        operation_store = {"add": add, "mul": mul, "sub": sub, "div": truediv}
        return reduce(lambda a, b : operation_store[operation](int(a), int(b)), elements)
    except:
        return f'Wrong input data'


print(custom_calculate(argv))