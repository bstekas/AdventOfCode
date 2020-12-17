# https://adventofcode.com/2020/day/15
from copy import deepcopy

DAY = 15

x_test = '''0,3,6'''
y_test = 436

y_test2 = None


# Part 1
def grow_list(start, N=2020):
    spoken = deepcopy(start)
    spoken.reverse()
    while len(spoken) < N:
        if spoken[0] in spoken[1::]:
            spoken.insert(0, spoken.index(spoken[0], 1))
        else:
            spoken.insert(0, 0)
    print(spoken)
    return spoken[0]


# Part 2
def grow_dict(start, N=30000000):
    spoken = {}
    seed = deepcopy(start)
    n = seed.pop()
    for k, v in enumerate(seed):
        spoken[v] = k

    i = len(seed)
    while i < N-1:
        if n in spoken.keys():
            i_old = spoken[n]
            spoken[n] = i
            n = i - i_old
        else:
            spoken[n] = i
            n = 0
        i += 1

    return n


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
    test_function(grow_list(x_test), y_test)

    print('\nInput Results:')
    test_function(grow_list(INPUT))

    if y_test2:
        print('\n----Part 2----')
        print('Test Results:')
        test_function(grow_dict(x_test), y_test2)

        print('\nInput Results:')
        # test_function(grow_list(INPUT))


if __name__ == '__main__':

    INPUT = [int(x) for x in "9,19,1,6,0,5,4".split(',')]
    x_test = [int(x) for x in x_test.split(',')]

    main(INPUT)