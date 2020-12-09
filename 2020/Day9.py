# https://adventofcode.com/2020/day/9
import copy

DAY = 9

x_test = '''5
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576'''.split('\n')
y_test = 127

y_test2 = 62


# Part 1
def parse_input(INPUT):
    INPUT = [int(i) for i in INPUT]
    l_preamb = INPUT.pop(0)

    return l_preamb, INPUT


def find_first_number(l_preamb, code):

    for i, num in enumerate(code[l_preamb::], start=l_preamb):
        valid = False
        for j in range(i-l_preamb, i-1):
            for k in range(i-l_preamb+1, i):
                if code[j] + code[k] == num:
                    valid = True

        if not valid:
            return num

    return None


# Part 2
def find_second_number(code, first_number):
    addends = [code[0]]
    i = 1
    while (sum(addends) < first_number) and i < len(code):
        addends.append(code[i])

        while sum(addends) > first_number:
            addends.pop(0)

        if sum(addends) == first_number:
            return min(addends) + max(addends)

        i += 1

    return None


def break_code(INPUT):
    l_preamb, code = parse_input(INPUT)

    first_number = find_first_number(l_preamb, code)
    second_number = find_second_number(code, first_number)

    return l_preamb, first_number, second_number


# Ingestion and Printing Results
def test_function(y_pred, y=None):
    if y:
        print('Output:', y_pred,
              '\tExpected:', y,
              '\tMatching?:', y_pred == y)
    else:
        print('Output:', y_pred)


def main(INPUT):

    test_preamb, test_first, test_second = break_code(x_test)
    input_preamb, input_first, input_second = break_code(INPUT)

    print('----Part 1----')
    print('Test Results:')
    print('Preamble size:', test_preamb)
    test_function(test_first, y_test)

    print('\nInput Results:')
    print('Preamble size:', input_preamb)
    test_function(input_first)

    if y_test2:
        print('\n----Part 2----')
        print('Test Results:')
        print('Preamble size:', test_preamb)
        test_function(test_second, y_test2)

        print('\nInput Results:')
        print('Preamble size:', input_preamb)
        test_function(input_second)


if __name__ == '__main__':
    INPUT = [25]
    f = open(f'./inputs/day{DAY}_input.txt')
    INPUT.extend(f.readlines())
    f.close()

    main(INPUT)