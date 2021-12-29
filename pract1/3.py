import sys


def check(parse, i, is_formula):
    if i == len(parse) or not is_formula:
        if is_formula:
            return True
        else:
            return False

    if parse[i] not in '+-' and not parse[i].isdigit():
        isFormula = False

    i += 1
    return check(parse, i, isFormula)

def main():
    parse = "".join(sys.argv[1:])
    if not len(parse) or not parse[0].isdigit() or not parse[len(parse) - 1].isdigit():
        isRight = False
    else:
        isRight = check(parse, 0, True)

    if isRight:
        print("True,", eval(parse))
    else:
        print("False, None")

main()