# https://adventofcode.com/2020/day/13
import re

DAY = 13

x_test = '''939
7,13,x,x,59,x,31,19'''.split('\n')
y_test = 295

y_test2 = 1068781


# Part 1
def find_earliest_bus(INPUT):
    t0 = int(INPUT[0])
    bus_ids = [int(x) for x in re.findall(r'\d+', INPUT[1])]

    t = t0
    while 1:
        for id in bus_ids:
            if t % id == 0:
                return (t-t0)*id
        t += 1


# Part 2
def time_valid(t, enum_bus_ids):
    valid = True
    for idx, bus_id in enum_bus_ids:
        if (t + idx) % bus_id != 0:
            valid = False
            break
    return valid


def find_time(buses, t0, factor):
    t = t0
    buses.sort(key=lambda x: x[1], reverse=True)

    while 1:
        if time_valid(t, buses):
            return t

        t += factor


def find_run_of_buses(INPUT):
    bus_ids = [(i, int(x)) for i, x in enumerate(INPUT[1].split(',')) if x != 'x']
    bus_ids.sort(key=lambda x: x[1], reverse=True)

    print('offsets:', [x for x, _ in bus_ids])
    print('bus ids:', [x for _, x in bus_ids])

    factor = bus_ids[0][1]
    t = factor - bus_ids[0][0]
    for i in range(1, len(bus_ids)):
        t = find_time(bus_ids[0:i+1], t, factor)
        factor = factor*bus_ids[i][1]

        print(t)

    return t


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
    test_function(find_earliest_bus(x_test), y_test)

    print('\nInput Results:')
    test_function(find_earliest_bus(INPUT))

    if y_test2:
        print('\n----Part 2----')
        print('Test Results:')
        test_function(find_run_of_buses(x_test), y_test2)

        print('\nInput Results:')
        test_function(find_run_of_buses(INPUT))


if __name__ == '__main__':
    f = open(f'./inputs/day{DAY}_input.txt')
    INPUT = f.readlines()
    f.close()

    main(INPUT)