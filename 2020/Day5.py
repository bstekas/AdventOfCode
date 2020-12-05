# https://adventofcode.com/2020/day/5
import re

DAY = 5

x_test = '''FBFBBFFRLR
BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL'''.split('\n')

y_test = 820

def find_seat(string):
    row_bin, col_bin =  re.match(r'^([F|B]{7})([L|R]{3})$', string).groups()
    row = int(row_bin.replace('F', '0').replace('B','1'), base=2)
    col = int(col_bin.replace('L', '0').replace('R','1'), base=2)
    return row, col


def get_seat_id(row, col):
    return 8*row + col

def run_part1(INPUT):
    ids = []
    for bpass in INPUT:
        ids.append(get_seat_id(*find_seat(bpass)))

    return max(ids)


def run_part2(INPUT):
    ids = []
    for bpass in INPUT:
        ids.append(get_seat_id(*find_seat(bpass)))

    ids.sort()
    for i in range(len(ids)-1):
        if ids[i+1] != ids[i]+1:
            return ids[i]+1


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
# Nothing to test for part 2

        print('Input Results:')
        print('Output:', run_part2(INPUT))


if __name__ == '__main__':
    f = open(f'./inputs/day{DAY}_input.txt')
    INPUT = f.read().split('\n')
    f.close()

    INPUT.remove('')

    main(INPUT)