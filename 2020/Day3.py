# https://adventofcode.com/2020/day/3

DAY = 3

x_test = '''
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#'''.split('\n')
x_test.remove('')

y_test = 7
y_test2 = 336


def run_slope(r, d, slope):
    width = len(slope[0])
    trees = 0

    i = 0
    j = 0

    while j < len(slope):
        row = slope[j]
        if row[i] == '#':
            trees += 1

        j += d
        if i+r >= width:
            i = (i+r)%(width)
        else:
            i = i+r

    return trees


def run_part1(slope):
    return run_slope(3, 1, slope)


def run_part2(slope):
    trees = 1
    for r, d in [(1,1), (3,1), (5,1), (7,1), (1,2)]:
        print(r, d)
        trees = trees*run_slope(r, d, slope)
    return trees


def main(INPUT):
    print('----Part 1----')
    print('Test Results:')
    print('Output:', run_part1(x_test),
          '\tExpected:', y_test,
          '\tMatching?:', run_part1(x_test) == y_test)

    print('\nInput Results:')
    print('Output:', run_part1(INPUT))

    print('\n----Part 2----')
    print('Test Results:')
    print('Output:', run_part2(x_test),
          '\tExpected:', y_test2,
          '\tMatching?:', run_part2(x_test) == y_test2)

    print('\nInput Results:')
    print('Output:', run_part2(INPUT))


if __name__ == '__main__':
    f = open(f'./inputs/day{DAY}_input.txt')
    INPUT = f.read().split('\n')
    f.close()

    INPUT.remove('')

    main(INPUT)

