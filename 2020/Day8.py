# https://adventofcode.com/2020/day/8
import copy

DAY = 8

x_test = '''nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6'''.split('\n')
y_test = 5

y_test2 = 8


# Part 1
def parse_lines(INPUT):
    output = []
    for i in INPUT:
        i = i.split()
        output.append([i[0], int(i[1])])

    return output


def execute_program(code):
    restart = False
    visited = []
    i = 0
    accumulator = 0

    while not restart:
        action, num = code[i]
        visited.append(i)
        if action in ['nop', 'acc']:
            if action == 'acc':
                accumulator += num
            i += 1
            if (i in visited) or (i == len(code)):
                restart = True
        elif action == 'jmp':
            i += num
            if (i in visited) or (i == len(code)):
                restart = True

    return accumulator, visited


def run_part1(code):
    accumulator, visited = execute_program(code)
    return accumulator


# Part 2
remap = {'jmp': 'nop',
         'nop': 'jmp'}


def run_part2(code):
    accumulator, visited = execute_program(code)
    m = max(visited)+1
    print(f'Executed to line {m} of {len(code)}')
    print(f'Traversed {len(visited)} lines')
    visited.reverse()

    for i in visited:
        new_code = copy.deepcopy(code)
        if new_code[i][0] in ('jmp', 'nop'):
            new_code[i][0] = remap[new_code[i][0]]
            accumulator, new_visited = execute_program(new_code)
            m = max(new_visited) + 1
            if m == len(code):
                print(f'\nExecuted all {len(code)} lines by changing line {i} from {code[i][0]} to {new_code[i][0]}')
                return accumulator

    return None


# Ingestion and Printing Results
def test_function(func, x, y=None):
    y_pred = func(x)

    if y:
        print('Output:', y_pred,
              '\tExpected:', y,
              '\tMatching?:', y_pred == y)
    else:
        print('Output:', y_pred)


def main(INPUT):
    print('----Part 1----')
    print('Test Results:')
    test_function(run_part1, x_test, y_test)

    print('\nInput Results:')
    test_function(run_part1, INPUT)

    if True:
        print('\n----Part 2----')
        print('Test Results:')
        test_function(run_part2, x_test, y_test2)

        print('\nInput Results:')
        test_function(run_part2, INPUT)


if __name__ == '__main__':
    f = open(f'./inputs/day{DAY}_input.txt')
    INPUT = f.readlines()
    f.close()

    INPUT = parse_lines(INPUT)
    x_test = parse_lines(x_test)

    main(INPUT)