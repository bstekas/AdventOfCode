# https://adventofcode.com/2020/day/18
import re

DAY = 18

x_test = '''2 * 3 + (4 * 5)
5 + (8 * 3 + 9 + 3 * 4 * 3)
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'''.split('\n')

y_test = 13632+12240+437+26


x_test2 = '''1 + (2 * 3) + (4 * (5 + 6))
2 * 3 + (4 * 5)
5 + (8 * 3 + 9 + 3 * 4 * 3)
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'''.split('\n')
y_test2 = 23340+669060+1445+46+51


# Part 1
def solve_eqn(eqn):
    if type(eqn) != str:
        eqn = eqn.groups()[-1]
    val = eqn[0]
    for c in eqn[1::]:
        val += c
        if val.count(' ') > 2:
            val = str(eval(val)) + ' '

    return str(eval(val))


def parse_pars(eqn):
    val = re.sub(r'\(([\d +*]+)\)', solve_eqn, eqn)
    if val.isnumeric():
        return int(val)
    if '(' in val:
        return parse_pars(val)
    else:
        return int(solve_eqn(val))


def do_homework(INPUT):
    vals = []
    for eqn in INPUT:
        vals.append(parse_pars(eqn))

    return sum(vals)


# Part 2
def do_mult(eqn):
    if type(eqn) != str:
        eqn = eqn.group(0)
    return str(eval(eqn))


def do_all_mult(eqn):
    val = re.sub(r'\d+ \+ \d+', do_mult, eqn, count=1)

    if re.findall(r'\d+ \+ \d+', val):
        return do_all_mult(val)
    else:
        return val


def parse_mult_pars(eqn):
    # print(1, eqn)
    val = do_all_mult(eqn)
    # print(2, val)
    val = re.sub(r'\(([\d +*]+)\)', solve_eqn, val)
    # print(2, val)
    if val.isnumeric():
        return int(val)
    elif ('(' in val) or ('+' in val):
        return parse_mult_pars(val)
    else:
        return int(solve_eqn(val))


def do_homework2(INPUT):
    vals = []
    for eqn in INPUT:
        vals.append(parse_mult_pars(eqn))
        # print(vals[-1], '\n')

    return sum(vals)

# Ingestion and Printing Results
def test_function(y_pred, y=None):
    if y:
        print('Output:', y_pred,
              '\tExpected:', y,
              '\tMatching?:', y_pred == y)
    else:
        print('Output:', y_pred)


def main(INPUT):

    print('\n----Part 1----')
    print('Test Results:')
    test_function(do_homework(x_test), y_test)

    print('\nInput Results:')
    test_function(do_homework(INPUT))

    if y_test2:
        print('\n----Part 2----')
        print('Test Results:')
        test_function(do_homework2(x_test2), y_test2)

        print('\nInput Results:')
        test_function(do_homework2(INPUT))


if __name__ == '__main__':
    f = open(f'./inputs/day{DAY}_input.txt')
    INPUT = f.readlines()
    f.close()

    main(INPUT)