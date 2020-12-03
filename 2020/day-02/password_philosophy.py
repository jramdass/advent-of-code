def read_input():
    values = []

    input = open("input")
    for line in input:
        values.append(line)

    return values

def is_password_valid_old(input):
    policy_min = int(input[:input.find('-')])
    policy_max = int(input[input.find('-')+1:input.find(' ')])
    policy_letter = input[input.find(' ')+1:input.find(':')]
    password = input[input.find(':')+2:]
 
    occurrences = password.count(policy_letter)

    if occurrences >= policy_min and occurrences <= policy_max:
        return True
    else: 
        return False

def is_password_valid_new(input):
    policy_pos1 = int(input[:input.find('-')]) - 1
    policy_pos2 = int(input[input.find('-')+1:input.find(' ')]) - 1
    policy_letter = input[input.find(' ')+1:input.find(':')]
    password = input[input.find(':')+2:]

    if password[policy_pos1] == policy_letter:
        if password[policy_pos2] == policy_letter:
            return False
        return True
    else:
        if password[policy_pos2] == policy_letter:
            return True

    return False

if __name__ == "__main__":
    values = read_input()

    # part 1
    count_occurrences = 0

    for input in values:
        if is_password_valid_old(input):
            count_occurrences += 1

    print(count_occurrences)

    # part 2
    count_occurrences = 0

    for input in values:
        if is_password_valid_new(input):
            count_occurrences += 1

    print(count_occurrences)
