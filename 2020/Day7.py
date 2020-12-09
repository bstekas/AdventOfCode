# https://adventofcode.com/2020/day/7

import re

DAY = 7

x_test = '''light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.'''.split('\n')
y_test = 4

y_test2 = 32


# Part 1
def parse_rule(rule_line):
    bags = re.findall(r'^([\w+ ]+) bags* contain', rule_line)[0]
    contains = re.findall(r'(\d+) ([\w+ ]+) bags*', rule_line)
    rules = {c: int(n) for n, c in contains}
    return {bags: rules}


def item_contained_in(item_set, rules):
    containers = set()
    for item in item_set:
        for k, v in rules.items():
            if item in v.keys():
                containers.add(k)
    if containers:
        return item_contained_in(containers - item_set, rules).union(item_set)

    else:
        return item_set


def run_part1(INPUT):
    rules = {}
    for rule in INPUT:
        rules.update(parse_rule(rule))

    return len(item_contained_in({'shiny gold'}, rules) - {'shiny gold'})


# Part 2
def item_contains(item, rules):
    if rules[item]:
        return sum([v*(1+item_contains(k, rules)) for k, v in rules[item].items()])
    else:
        return 0


def run_part2(INPUT):
    rules = {}
    for rule in INPUT:
        rules.update(parse_rule(rule))

    return item_contains('shiny gold', rules)


# Ingestion and Printing Results
def test_function(func, x, *y):
    y_pred = func(x)

    if y:
        print('Output:', y_pred,
              '\tExpected:', y[0],
              '\tMatching?:', y_pred == y[0])
    else:
        print('Output:', y_pred)


def main(INPUT):
    print('----Part 1----')
    print('Test Results:')
    test_function(run_part1, x_test, y_test)

    print('\nInput Results:')
    test_function(run_part1, INPUT)

    if True:
        print('\n----Part 2----')
        print('Test Results:')
        test_function(run_part2, x_test, y_test2)

        print('\nInput Results:')
        test_function(run_part2, INPUT)


if __name__ == '__main__':
    f = open(f'./inputs/day{DAY}_input.txt')
    INPUT = f.readlines()
    f.close()

    main(INPUT)