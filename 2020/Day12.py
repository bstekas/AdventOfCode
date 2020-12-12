# https://adventofcode.com/2020/day/12
import re
import math

DAY = 12

x_test = '''F10
N3
F7
R90
F11'''.split()
y_test = 25

y_test2 = 286


dir_map = {'N': (1, 1),
           'S': (-1, 1),
           'E': (1, 0),
           'W': (-1, 0)}

directions = list('NESW')
turn_map = {'L': -1,
            'R': +1}

# Part 1
class Ship(object):
    def __init__(self, heading, location=None):
        if location:
            self.location = location
        else:
            self.location = [0, 0]
        self.heading = heading

    def move(self, d, m):
        if d == 'F':
            d = self.heading

        sgn, pos = dir_map[d]
        self.location[pos] += sgn*m

    def change_course(self, d, m):
        current_ind = directions.index(self.heading)
        new_ind = (current_ind + turn_map[d]*int(m/90)) % len(directions)
        self.heading = directions[new_ind]


def follow_instructions(instructions, heading='E'):
    ship = Ship(heading, [0, 0])
    for inst in instructions:
        d, m = re.match(r'([NESWLRF])(\d+)', inst).groups()
        m = int(m)

        if d in ('L', 'R'):
            ship.change_course(d, m)
        else:
            ship.move(d, m)

    return abs(ship.location[0]) + abs(ship.location[1])


# Part 2
quadrant_signs = {1: (1, 1),
                  2: (1, -1),
                  3: (-1, -1),
                  4: (-1, 1)}


def get_quadrant(x, y):
    if x >= 0:
        if y >=0:
            return 1
        else:
            return 2
    else:
        if y >=0:
            return 4
        else:
            return 3


class Ship2(object):
    def __init__(self, location=None, waypoint=None):
        if location:
            self.location = location
        else:
            self.location = [0, 0]

        if waypoint:
            self.waypoint = waypoint
        else:
            self.waypoint = [10, 1]

    def move_waypoint(self, d, m):
        sgn, pos = dir_map[d]
        self.waypoint[pos] += sgn * m

    def rotate_waypoint(self, d, m):
        x, y = self.waypoint

        try:
            theta0 = math.atan(self.waypoint[1]/self.waypoint[0])*180/math.pi
        except ZeroDivisionError:
            theta0 = math.copysign(90, self.waypoint[1])

        if x < 0:  # atan() give results between -pi/2 and pi/2
            theta0 = theta0 + math.copysign(1, y)*180

        l = math.sqrt(self.waypoint[1]**2 + self.waypoint[0]**2)

        theta = theta0 - turn_map[d]*m  # sign flip!
        # print(d, m, theta0, theta)
        # print(self.waypoint)
        self.waypoint[0] = round(l * math.cos(theta * math.pi/180), 2)  # safe for this puzzle(?), but precision can really change the outcome
        self.waypoint[1] = round(l * math.sin(theta * math.pi/180), 2)
        # print(self.waypoint)
        # print()

    def move(self, n):
        self.location[0] += n * self.waypoint[0]
        self.location[1] += n * self.waypoint[1]

    def rotate_quadrant(self, d, m):
        n = int(m/90)  # this only works for multiples of 90
        x, y = self.waypoint

        curr_q = get_quadrant(x, y)
        next_q = (curr_q + turn_map[d]*n) % 4
        if next_q == 0:
            next_q = 4

        next_sgn_x, next_sgn_y = quadrant_signs[next_q]

        self.waypoint[0] = next_sgn_x*abs([x, y][n % 2])
        self.waypoint[1] = next_sgn_y*abs([y, x][n % 2])


def follow_waypoint(instructions, quad=False):
    ship = Ship2()
    print('Starting location:', ship.location, 'heading:', ship.waypoint)
    for i, inst in enumerate(instructions):
        d, m = re.match(r'([NESWLRF])(\d+)', inst).groups()
        m = int(m)

        if d in ('L', 'R'):
            if quad:
                ship.rotate_quadrant(d, m)
            else:
                ship.rotate_waypoint(d, m)  # rotate_waypoint,  rotate_quadrant

        elif d == 'F':
            ship.move(m)
        else:
            ship.move_waypoint(d, m)

    print('Ending location:', ship.location, 'heading:', ship.waypoint)

    return abs(ship.location[0]) + abs(ship.location[1])


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
    test_function(follow_instructions(x_test), y_test)

    print('\nInput Results:')
    test_function(follow_instructions(INPUT))

    if y_test2:
        print('\n----Part 2----')
        print('Test Results:')
        test_function(follow_waypoint(x_test), y_test2)

        print('\nInput Results:')
        test_function(follow_waypoint(INPUT))
        test_function(follow_waypoint(INPUT, quad=True))


if __name__ == '__main__':
    f = open(f'./inputs/day{DAY}_input.txt')
    INPUT = f.readlines()
    f.close()

    main(INPUT)