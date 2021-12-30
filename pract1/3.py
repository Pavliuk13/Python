import sys


def check(parse, i, is_formula):
    if i == len(parse) or not is_formula:
        return is_formula

    if parse[i] not in '+-' and not parse[i].isdigit():
        is_formula = False

    i += 1
    return check(parse, i, is_formula)


def main():
    parse = "".join(sys.argv[1:])
    if not len(parse) or not parse[0].isdigit() or not parse[len(parse) - 1].isdigit():
        is_right = False
    else:
        is_right = check(parse, 0, True)

    if is_right:
        print("True,", eval(parse))
    else:
        print("False, None")

main()