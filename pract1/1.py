from sys import argv


def calculate(user_input): 
    if len(user_input):
        return eval(''.join(argv[1:]))


def main():
    try:
        print(calculate(argv[1:]))
    except Exception as ex:
        print(ex)