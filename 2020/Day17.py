# https://adventofcode.com/2020/day/17
import math as m

DAY = 17

x_test = '''.#.
..#
###'''.split('\n')

y_test = 112

y_test2 = 848


# Part 1
class Pocket2Dimension(object):
    def __init__(self, INPUT):
        INPUT.reverse()
        self.active_cubes = set()
        self.accessible_cubes = {}

        for j, inp in enumerate(INPUT):
            for i, c in enumerate(list(inp)):
                if c == '#':
                    self.active_cubes.add((i, j, 0))

        self.count_active_neighbors()

    def find_accessible_cubes(self):
        for x, y, z in self.active_cubes:
            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    for k in range(z - 1, z + 2):
                        self.accessible_cubes[(i, j, k)] = 0

    def n_active(self):
        return len(self.active_cubes)

    def print_z(self, z0):
        locs = []
        xlocs = []
        ylocs = []
        print()
        for x, y, z in self.active_cubes:
            if z == z0:
                locs.append((x, y))
                xlocs.append(x)
                ylocs.append(y)
        print('x min:', min(xlocs))
        for y in reversed(range(min(ylocs), max(ylocs)+1)):
            line = ''
            for x in range(min(xlocs), max(xlocs)+1):
                if (x,y) in locs:
                    line += '#'
                else:
                    line += '.'
            print(y, '\t',line)

    def count_active_neighbors(self):
        self.find_accessible_cubes()

        for x, y, z in self.accessible_cubes.keys():
            self.accessible_cubes[(x, y, z)] = 0
            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    for k in range(z - 1, z + 2):
                        if ((i, j, k) in self.active_cubes) & ((i, j, k) != (x, y, z)):
                            self.accessible_cubes[(x, y, z)] += 1

    def cycle(self):
        for loc, n in self.accessible_cubes.items():
            active = loc in self.active_cubes

            if active and (n not in (2, 3)):
                self.active_cubes.remove(loc)
            if not active and (n == 3):
                self.active_cubes.add(loc)

        self.count_active_neighbors()


def run_cycles(INPUT, n=6):
    pocket = Pocket2Dimension(INPUT)
    pocket.print_z(0)
    print(0, pocket.n_active())
    for i in range(6):
        pocket.cycle()
        # pocket.print_z(0)
        print(i+1, pocket.n_active())
    return pocket.n_active()


# Part 2
class Pocket3Dimension(object):
    def __init__(self, INPUT):
        INPUT.reverse()
        self.active_cubes = set()
        self.accessible_cubes = {}

        for j, inp in enumerate(INPUT):
            for i, c in enumerate(list(inp)):
                if c == '#':
                    self.active_cubes.add((i, j, 0, 0))

        self.count_active_neighbors()

    def find_accessible_cubes(self):
        self.accessible_cubes = {}
        for x, y, z, w in self.active_cubes:
            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    for k in range(z - 1, z + 2):
                        for m in range(w - 1, w + 2):
                            self.accessible_cubes[(i, j, k, m)] = 0

    def n_active(self):
        return len(self.active_cubes)

    def print_z(self, z0, w0):
        locs = []
        xlocs = []
        ylocs = []
        print()
        for x, y, z, w in self.active_cubes:
            if (z == z0) & (w == w0):
                locs.append((x, y))
                xlocs.append(x)
                ylocs.append(y)
        print('x min:', min(xlocs))
        for y in reversed(range(min(ylocs), max(ylocs)+1)):
            line = ''
            for x in range(min(xlocs), max(xlocs)+1):
                if (x,y) in locs:
                    line += '#'
                else:
                    line += '.'
            print(y, '\t', line)

    def count_active_neighbors(self):
        self.find_accessible_cubes()

        for x, y, z, w in self.accessible_cubes.keys():
            self.accessible_cubes[(x, y, z, w)] = 0
            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    for k in range(z - 1, z + 2):
                        for m in range(w - 1, w + 2):
                            if ((i, j, k, m) in self.active_cubes) & ((i, j, k, m) != (x, y, z, w)):
                                self.accessible_cubes[(x, y, z, w)] += 1

    def cycle(self):
        for loc, n in self.accessible_cubes.items():
            active = loc in self.active_cubes

            if active and (n not in (2, 3)):
                self.active_cubes.remove(loc)
            if not active and (n == 3):
                self.active_cubes.add(loc)

        self.count_active_neighbors()


def run_cycles_3D(INPUT, n=6):
    pocket = Pocket3Dimension(INPUT)
    pocket.print_z(0,0)
    print(0, pocket.n_active())
    for i in range(6):
        pocket.cycle()
        # pocket.print_z(0)
        print(i+1, pocket.n_active())
    return pocket.n_active()


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
    test_function(run_cycles(x_test), y_test)

    print('\nInput Results:')
    test_function(run_cycles(INPUT))

    if y_test2:
        print('\n----Part 2----')
        print('Test Results:')
        test_function(run_cycles_3D(x_test), y_test2)

        print('\nInput Results:')
        test_function(run_cycles_3D(INPUT))


if __name__ == '__main__':
    f = open(f'./inputs/day{DAY}_input.txt')
    INPUT = f.readlines()
    f.close()

    main(INPUT)