# https://adventofcode.com/2020/day/11
import copy

DAY = 11

x_test = '''L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL'''.split()
y_test = 37

y_test2 = 26

# print("\n".join(x_test))


# Part 1
def get_seat_state(i, j, seats):
    occupied = False
    if seats[i][j] == '#':
        occupied = True
    return occupied


def find_adjacent_seats(k, l, seats):
    neighbors = []
    neighbor_states = []

    for i in range(k-1, k+2):
        if (i >= 0) & (i < len(seats)):
            for j in range(l-1, l+2):
                if (j >= 0) & (j < len(seats[i])) & ~(( j== l) & (i == k)):
                    neighbors.append((i, j))
                    # print(neighbors == '#')
                    neighbor_states.append(get_seat_state(i, j, seats))
    # print(k, l, len(neighbors))
    return neighbor_states, neighbors


def seating_round(seats):
    new_seats = copy.deepcopy(seats)
    for i in range(len(seats)):
        new_seats[i] = list(seats[i])
        for j in range(len(seats[i])):
            if seats[i][j] != '.':
                neighbor_states, _ = find_adjacent_seats(i, j, seats)
                if (seats[i][j] == '#') & (sum(neighbor_states) >= 4):
                    new_seats[i][j] = 'L'
                elif (seats[i][j] == 'L') & (sum(neighbor_states) == 0):
                    new_seats[i][j] = '#'

        new_seats[i] = "".join(new_seats[i])

    return new_seats


def run_part1(seats):
    new_seats = copy.deepcopy(seats)
    last_seats = copy.deepcopy(new_seats)
    n = 0

    while new_seats != last_seats or n < 2:
        n += 1
        last_seats = copy.deepcopy(new_seats)
        new_seats = seating_round(new_seats)
        if (n % 10) == 0:
            occ = "".join(new_seats).count('#')
            print(f"round {n} with {occ} seats occupied")
            # print("\n".join(new_seats))

    return "".join(new_seats).count('#')


# Part 2
def find_visible_seats(k, l, seats):
    neighbors = []
    neighbor_states = []

    # N
    for i in reversed(range(k)):
        j = l
        if seats[i][j] != '.':
            neighbors.append((i, j))
            neighbor_states.append(get_seat_state(i, j, seats))
            break

    # S
    for i in range(k+1, len(seats)):
        j = l
        if seats[i][j] != '.':
            neighbors.append((i, j))
            neighbor_states.append(get_seat_state(i, j, seats))
            break

    # E
    i = k
    for j in range(l+1, len(seats[i])):
        if seats[i][j] != '.':
            neighbors.append((i, j))
            neighbor_states.append(get_seat_state(i, j, seats))
            break

    # W
    i = k
    for j in reversed(range(l)):
        if seats[i][j] != '.':
            neighbors.append((i, j))
            neighbor_states.append(get_seat_state(i, j, seats))
            break

    # NE
    for d in range(1, min([k+1, len(seats[k]) - l])):
        i = k - d
        j = l + d
        if seats[i][j] != '.':
            neighbors.append((i, j))
            neighbor_states.append(get_seat_state(i, j, seats))
            break

    # NW
    for d in range(1, min(k+1, l+1)):
        i = k-d
        j = l-d
        if seats[i][j] != '.':
            neighbors.append((i, j))
            neighbor_states.append(get_seat_state(i, j, seats))
            break

    # SE
    for d in range(1, min([len(seats)-k, len(seats[k])-l])):
        i = k+d
        j = l+d
        if seats[i][j] != '.':
            neighbors.append((i, j))
            neighbor_states.append(get_seat_state(i, j, seats))
            break

    # SW
    for d in range(1, min([len(seats)-k, l+1])):
        i = k+d
        j = l-d
        if seats[i][j] != '.':
            neighbors.append((i, j))
            neighbor_states.append(get_seat_state(i, j, seats))
            break

    return neighbor_states, neighbors


def seating_round2(seats, neighbor_map=None):
    new_seats = copy.deepcopy(seats)

    if neighbor_map is None:
        # only get list of neighbors on the first round
        neighbor_map = {}

        for i in range(len(seats)):
            # new_seats[i] = list(seats[i])
            for j in range(len(seats[i])):
                if seats[i][j] != '.':
                    neighbor_states, neighbors = find_visible_seats(i, j, seats)
                    # print((i, j), len(neighbors), neighbors)
                    neighbor_map[(i, j)] = neighbors

                    if (seats[i][j] == '#') & (sum(neighbor_states) >= 5):
                        new_seats[i][j] = 'L'
                    elif (seats[i][j] == 'L') & (sum(neighbor_states) == 0):
                        new_seats[i][j] = '#'

    else:
        # use list of neighbors in subsequent rounds
        # saving this doesn't work for my input, but I have no idea why
        for i, j in neighbor_map.keys():
            neighbor_states = [get_seat_state(*ind, seats) for ind in neighbor_map[(i, j)]]
            if (seats[i][j] == '#') & (sum(neighbor_states) >= 5):
                new_seats[i][j] = 'L'
            elif (seats[i][j] == 'L') & (sum(neighbor_states) == 0):
                new_seats[i][j] = '#'

    return new_seats, neighbor_map


def run_part2(seats):
    seats = [list(x) for x in seats]
    new_seats = copy.deepcopy(seats)
    neighbor_map = None
    n = 0

    while n < 1 or new_seats != last_seats:
        n += 1
        last_seats = copy.deepcopy(new_seats)
        new_seats, neighbor_map = seating_round2(new_seats, neighbor_map=None)

        # print("\n".join(["".join(x) for x in new_seats]))

        if (n % 10) == 0:
            # print("\n".join(["".join(x) for x in new_seats]))
            occ = "".join(["".join(x) for x in new_seats]).count('#')
            print(f"round {n} with {occ} seats occupied")

    return "".join(["".join(x) for x in new_seats]).count('#')


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
    print('Test Results:\n')
    test_function(run_part1(x_test), y_test)

    print('\nInput Results:')
    test_function(run_part1(INPUT))

    if y_test2:
        print('\n----Part 2----')
        print('Test Results:')
        test_function(run_part2(x_test), y_test2)

        print('\nInput Results:')
        test_function(run_part2(INPUT))


if __name__ == '__main__':
    f = open(f'./inputs/day{DAY}_input.txt')
    INPUT = f.readlines()
    f.close()

    main(INPUT)