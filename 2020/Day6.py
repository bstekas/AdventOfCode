# https://adventofcode.com/2020/day/6
import re

DAY = 6

x_test = '''abc

a
b
c

ab
ac

a
a
a
a

b'''.split('\n\n')
y_test = 11

y_test2 = 6

def find_union_answers(string):
    family = string.split()
    answers = set()
    for member in family:
        answers = answers | set(member)
    return len(answers)


def find_intersect_answers(string):
    family = string.split()
    answers = set(family[0])
    for member in family[1:]:
        answers = answers & set(member)
    return len(answers)


def run_part1(INPUT):
    answers = []
    for family in INPUT:
        answers.append(find_union_answers(family))

    return sum(answers)


def run_part2(INPUT):
    answers = []
    for family in INPUT:
        answers.append(find_intersect_answers(family))

    return sum(answers)


def main(INPUT):
    print('----Part 1----')
    print('Test Results:')
    print('Output:', run_part1(x_test),
          '\tExpected:', y_test,
          '\tMatching?:', run_part1(x_test) == y_test)

    print('\nInput Results:')
    print('Output:', run_part1(INPUT))

    if True:
        print('\n----Part 2----')
        print('Test Results:')
        print('Output:', run_part2(x_test),
              '\tExpected:', y_test2,
              '\tMatching?:', run_part2(x_test) == y_test2)

        print('\nInput Results:')
        print('Output:', run_part2(INPUT))


if __name__ == '__main__':
    f = open(f'./inputs/day{DAY}_input.txt')
    INPUT = f.read().split('\n\n')
    f.close()

    main(INPUT)