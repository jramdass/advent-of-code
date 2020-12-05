"""
Day 04
I had some trouble with this one. I knew that there were much better ways to do it
than my original approach but I don't know regex that well.
I went back after finishing and took the opportunity to learn and try out regex.
I made a comment wherever I changed my original solution.
"""

import re

def read_input():
    values = []

    input = open("input")
    for line in input:
        values.append(line)

    return values

def extract_passports(values):
    passport = []
    passports = []
    i = 0 

    while i < len(values):
        for j in range (i, len(values)):
            if values[j] == '\n':
                break
            passport.append(values[j])
        passports.append(passport)
        passport = []
        i = j+1

    return passports

def verify_passport(passport):
    parameter_list = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    parameters_found = 0

    for parameter in parameter_list:
        for i in range (0, len(passport)):
            if passport[i].find(parameter) >= 0:
                parameters_found += 1  

    if parameters_found == len(parameter_list):
        return True
    else:
        return False

def convert_passport_to_dict(passport):
    passport_dict = {}
    
    # index = 0
    # for i in range (0, len(passport)):
    #     while index >= 0:
    #         if passport[i].find('\n') < 0 and passport[i].find(' ') < 0:
    #             passport_dict[passport[i][:passport[i].find(':')]] = passport[i][passport[i].find(':')+1:]
    #             index = -1
    #         else:
    #             passport_dict[passport[i][:passport[i].find(':')]] = passport[i][passport[i].find(':')+1:passport[i].find(' ')]
    #             index = passport[i].find(' ')
    #         passport[i] = passport[i][index+1:]
    #     index = 0

    # Added after completion
    for i in range (0, len(passport)):
        list_pairs = re.findall('[a-z]{3}:\S+', passport[i])
        for pair in list_pairs:
            passport_dict[pair[:pair.find(':')]] = pair[pair.find(':')+1:]
    
    return passport_dict

def verify_passport_valid_fields(passport):
    if 'cid' in passport:
        if len(passport) != 8:
            return False
    else:
        if len(passport) != 7:
            return False

    for key in passport:
        if key == 'byr':
            if int(passport[key]) < 1920 or int(passport[key]) > 2002:
                return False
        if key == 'iyr':
            if int(passport[key]) < 2010 or int(passport[key]) > 2020:
                return False
        if key == 'eyr':
            if int(passport[key]) < 2020 or int(passport[key]) > 2030:
                return False
        if key == 'hgt':
            # if passport[key].find('cm') >= 0:
            #     height = int(passport[key][:passport[key].find('cm')])
            #     if height < 150 or height > 193:
            #         return False
            # elif passport[key].find('in') >= 0:
            #     height = int(passport[key][:passport[key].find('in')])
            #     if height < 59 or height > 76:
            #         return False
            # else:
            #     return False

            # Added after completion X
            if re.match('^((1[5-8][0-9])|(19[0-3]))cm$|^(59|6[0-9]|7[0-6])in$', passport[key]) is None:
                return False
        if key == 'hcl':
            # if passport[key][0] != '#':
            #     return False
            # passport[key] = passport[key][1:]
            # if len(passport[key]) != 6:
            #     return False
            # for char in passport[key]:
            #     if char not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']:
            #         return False

            # Added after completion
            if re.match('^#[a-f0-9]{6}$', passport[key]) is None:
                return False
        if key == 'ecl':
            if passport[key] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                return False
        if key == 'pid':
            # if len(passport[key]) != 9:
            #     return False
            # for char in passport[key]:
            #     if char not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            #         return False

            # Added after completion X
            if re.match('^\d{9}$', passport[key]) is None:
                return False

    return True


if __name__ == "__main__":
    values = read_input()

    # part 1
    valid_passport_count = 0

    passports = extract_passports(values)

    for passport in passports:
        if verify_passport(passport):
            valid_passport_count += 1

    print(valid_passport_count)

    # part 2
    valid_passport_count = 0

    for passport in passports:
        new_passport = convert_passport_to_dict(passport)
        if verify_passport_valid_fields(new_passport):
            valid_passport_count += 1

    print(valid_passport_count)
