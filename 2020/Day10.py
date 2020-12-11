# https://adventofcode.com/2020/day/10
import math as m

DAY = 10

x_test = '''28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3'''.split('\n')
y_test = 22*10

y_test2 = 19208


# Part 1
def count_diffs(adapters):
    adapters.sort()

    n = [0, 0, 1]
    last = 0
    for a in adapters:
        n[a-last-1] += 1
        last = a

    return n[0]*n[2]


# Part 2
def count_branches(n, adapters, known_branches):
    branches = 0
    any0 = False

    for d in [1, 2, 3]:
        if n - d in adapters:
            branches += known_branches[n-d]
        elif n - d <= 0:
            any0 = True
    if any0:
        branches += 1
    return branches


def make_tree(adapters):
    known_branches = {}

    for a in adapters:
        known_branches[a] = count_branches(a, adapters, known_branches)

    return known_branches[max(adapters)]


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
    test_function(count_diffs(x_test), y_test)

    print('\nInput Results:')
    test_function(count_diffs(INPUT))

    if y_test2:
        print('\n----Part 2----')
        print('Test Results:')
        test_function(make_tree(x_test), y_test2)

        print('\nInput Results:')
        test_function(make_tree(INPUT))


if __name__ == '__main__':
    f = open(f'./inputs/day{DAY}_input.txt')
    INPUT = f.readlines()
    f.close()

    INPUT = [int(i) for i in INPUT]
    x_test = [int(i) for i in x_test]

    main(INPUT)