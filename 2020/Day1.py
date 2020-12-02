# ----- Day 1: Report Repair -----
# After saving Christmas five years in a row, you've decided to take a 
# vacation at a nice resort on a tropical island. Surely, Christmas will go 
# on without you.

# The tropical island has its own currency and is entirely cash-only. The gold 
# coins used there have a little picture of a starfish; the locals just call 
# them stars. None of the currency exchanges seem to have heard of them, but 
# somehow, you'll need to find fifty of these coins by the time you arrive so 
# you can pay the deposit on your room.

# To save your vacation, you need to get all fifty stars by December 25th.

# Collect stars by solving puzzles. Two puzzles will be made available on each 
# day in the Advent calendar; the second puzzle is unlocked when you complete 
# the first. Each puzzle grants one star. Good luck!

# Before you leave, the Elves in accounting just need you to fix your expense 
# report (your puzzle input); apparently, something isn't quite adding up.

# Specifically, they need you to find the two entries that sum to 2020 and then 
# multiply those two numbers together.

# For example, suppose your expense report contained the following:

# 1721
# 979
# 366
# 299
# 675
# 1456

# In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying 
# them together produces 1721 * 299 = 514579, so the correct answer is 514579.

# Of course, your expense report is much larger. Find the two entries that sum 
# to 2020; what do you get if you multiply them together?

# ----- Part Two -----
# The Elves in accounting are thankful for your help; one of them even offers 
# you a starfish coin they had left over from a past vacation. They offer you a 
# second one if you can find three numbers in your expense report that meet the 
# same criteria.

# Using the above example again, the three entries that sum to 2020 are 979, 366, 
# and 675. Multiplying them together produces the answer, 241861950.

# In your expense report, what is the product of the three entries that sum to 2020?


x_test = [1721,979,366,299,675,1456]
y_test = 514579
y_test2 = 241861950

def get_factors(expenses):
    for i in range(len(expenses)-1):
        for j in range(i+1, len(expenses)):
            if expenses[i] + expenses[j] == 2020:
                return expenses[i]*expenses[j]


def get_three_factors(expenses):
    for i in range(len(expenses)-2):
        for j in range(i+1, len(expenses)-1):
            for k in range(j+1, len(expenses)):
                if expenses[i] + expenses[j] + expenses[k] == 2020:
                    return expenses[i]*expenses[j]*expenses[k]
            

def run_part1(expenses):
    print('Test Results')
    ty = get_factors(x_test)
    print('Output:', ty,
        '\tExpected:', y_test,
        '\tMactching?:', y_test==ty)

    print('\nInput Results')
    ty = get_factors(expenses)
    print('Output:', ty)


def run_part2(expenses):
    print('Test Results')
    ty = get_three_factors(x_test)
    print('Output:', ty,
        '\tExpected:', y_test2,
        '\tMactching?:', y_test2==ty)

    print('\nInput Results')
    ty = get_three_factors(expenses)
    print('Output:', ty)


def main(expenses):
    print('-----Part 1 Results-----')
    run_part1(expenses)

    print('\n-----Part 2 Results-----')
    run_part2(expenses)


if __name__ in '__main__':
    f = open('./inputs/input_day1.txt')
    INPUT = f.read().split('\n')
    f.close()

    INPUT.remove('')
    INPUT = [int(x) for x in INPUT]

    main(INPUT)
