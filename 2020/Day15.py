# https://adventofcode.com/2020/day/15

DAY = 15

x_test = '''0,3,6'''
y_test = 436

y_test2 = 175594


def list_lookup(start, N=2020):
    print('Seed list:', start)
    last_used = [-1]*N
    spoken = []
    for i, n in enumerate(start):
        last_used[n] = i
        spoken.append(n)

    last_used[n] = -1
    new_n = spoken.pop()
    while i < N:
        n = new_n
        if last_used[n] == -1:
            new_n = 0
        else:
            new_n = i - last_used[n]

        # spoken.append(n)
        last_used[n] = i
        i = i+1

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
    test_function(list_lookup(x_test, N=2020), y_test)

    print('\nInput Results:')
    test_function(list_lookup(INPUT, N=2020))

    if y_test2:
        print('\n----Part 2----')
        print('Test Results:')
        test_function(list_lookup(x_test, N=30000000), y_test2)

        print('\nInput Results:')
        test_function(list_lookup(INPUT, N=30000000))


if __name__ == '__main__':

    INPUT = [int(x) for x in "9,19,1,6,0,5,4".split(',')]
    x_test = [int(x) for x in x_test.split(',')]

    main(INPUT)