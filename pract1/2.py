from sys import argv
from functools import reduce
from operator import add, sub, mul, truediv


def custom_calculate(user_input):
    operations = {'add': add, 'sub': sub, 'mul': mul, 'div': truediv}
    operatorUse = user_input[1]
    nums = user_input[2:]
    try:
        operations[operatorUse]
        return reduce(lambda a, b: operations.get(operatorUse)(int(a), int(b)), nums)
    except:
        return f'Wrong input data'


print(custom_calculate(argv))