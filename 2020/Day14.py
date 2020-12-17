# https://adventofcode.com/2020/day/14
import re

DAY = 14

x_test = '''mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0'''.split('\n')
y_test = 165

x_test2 = '''mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1'''.split('\n')

y_test2 = 208


# Part 1
def parse_input(INPUT):
    program = []
    for step in INPUT:
        if 'mask' in step:
            mask = re.findall(r'[X10]{36}', step)[0]
            program.append(('mask', mask))

        elif 'mem' in step:
            mem = re.findall(r'\[(\d+)\] = (\d+)', step)[0]
            program.append(('mem', *mem))

    return program


def mask_number(num, mask):
    num = list('{0:036b}'.format(int(num)))
    for i, v in mask.items():
        num[i] = v
    return ''.join(num)


def execute_program(program):
    mask = ''
    memory = {}
    for step in program:
        if step[0] == 'mask':
            mask = {k: v for k, v in enumerate(list(step[1])) if v != 'X'}
        elif step[0] == 'mem':
            _, idx, num = step
            num = mask_number(num, mask)
            memory[int(idx)] = num

    # print('Final values stored in memory')
    # print(memory)
    s = 0
    for v in memory.values():
        s += int(v, 2)
    return s


# Part 2
def parse_wild_ints(val):
    if val.isdigit():
        # print(val, int(val, 2))
        return [int(val, 2)]
    else:
        return parse_wild_ints(val.replace('X', '0', 1)) + parse_wild_ints(val.replace('X', '1', 1))


def execute_program2(program):
    mask = ''
    memory = {}
    for step in program:
        if step[0] == 'mask':
            # print(step[1])
            mask = {k: v for k, v in enumerate(list(step[1])) if v != '0'}
        elif step[0] == 'mem':
            _, idx, val = step
            idx = mask_number(idx, mask)
            idx = parse_wild_ints(idx)
            # print(idx)
            for i in idx:
                memory[i] = int(val)

    # print('Final values stored in memory')
    # print(memory)
    s = 0
    for v in memory.values():
        s += v
    return s


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
    test_function(execute_program(parse_input(x_test)), y_test)

    print('\nInput Results:')
    test_function(execute_program(parse_input(INPUT)))

    if y_test2:
        print('\n----Part 2----')
        print('Test Results:')
        test_function(execute_program2(parse_input(x_test2)), y_test2)

        print('\nInput Results:')
        test_function(execute_program2(parse_input(INPUT)))


if __name__ == '__main__':
    f = open(f'./inputs/day{DAY}_input.txt')
    INPUT = f.readlines()
    f.close()

    main(INPUT)