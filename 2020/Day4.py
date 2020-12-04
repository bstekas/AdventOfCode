# https://adventofcode.com/2020/day/4
import re

DAY = 4

x_test = '''ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in'''.split('\n\n')

y_test = 2


x_test2 = '''eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007

pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719'''.split('\n\n')
y_test2 = 4

all_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'}


def split_fields(passport):
    return {k: v for k, v in re.findall(r'(\w+):(\S+)', passport)}


def has_needed_fields(pass_dict, fields):
    if set(pass_dict.keys()).issuperset(fields):
        return True
    else:
        return False


def check_date(v, mini, maxi):
    if re.fullmatch(r'^(\d{4})$', v):
        return (int(v) >= mini) and (int(v) <= maxi)
    else:
        return False


def fields_valid(pass_dict):
    for k, v in pass_dict.items():
        if k == 'byr':
            if not check_date(v, 1920, 2002):
                return False

        elif k == 'iyr':
            if not check_date(v, 2010, 2020):
                return False

        elif k == 'eyr':
            if not check_date(v, 2020, 2030):
                return False

        elif k == 'hgt':
            if re.fullmatch(r'^(\d+)(cm|in)$', v) :
                h, u = re.fullmatch(r'^(\d+)(cm|in)$', v).groups()
                if u == 'cm':
                    if int(h) < 150 or int(h) > 193:
                        return False

                elif u == 'in':
                    if int(h) < 59 or int(h) > 76:
                        return False

            else:
                return False

        elif k == 'hcl':
            if re.fullmatch(r'^#[a-f0-9]{6}$', v) is None:
                return False

        elif k == 'ecl':
            if v not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                return False

        elif k == 'pid':
            if re.fullmatch(r'^\d{9}$', v) is None:
                return False

    return True



def run_part1(INPUT):
    fields = all_fields - {'cid'}
    validity = []
    for passport in INPUT:
        validity.append(has_needed_fields(split_fields(passport), fields))

    return sum(validity)


def run_part2(INPUT):
    fields = all_fields - {'cid'}
    validity = []
    for passport in INPUT:
        pass_dict = split_fields(passport)
        if has_needed_fields(pass_dict, fields):
            validity.append(fields_valid(pass_dict))
        else:
            validity.append(False)

    # print(validity)
    return sum(validity)


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
        print('Test Results:')
        print('Output:', run_part2(x_test2),
              '\tExpected:', y_test2,
              '\tMatching?:', run_part2(x_test2) == y_test2)

        print('\nInput Results:')
        print('Output:', run_part2(INPUT))


if __name__ == '__main__':
    f = open(f'./inputs/day{DAY}_input.txt')
    INPUT = f.read().split('\n\n')
    f.close()

    main(INPUT)