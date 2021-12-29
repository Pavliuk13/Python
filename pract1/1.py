from sys import argv


def calculate(user_input): 
    if len(user_input):
        try:
            return eval(''.join(argv[1:]))
        except:
            return f'Wrong input data'

print(calculate(argv[1:]))