def read_input():
    values = []

    input = open("input")
    for line in input:
        values.append(line)

    return values

def split_into_groups(values):
    group = []    
    all_groups = []

    for line in values:
        if line != '\n':
            group.append(line)
        else:
            all_groups.append(group)
            group = []

    all_groups.append(group)

    return all_groups

def count_unique_answers(group):
    count = [0] * 26
    total_count = 0

    allchars = 'abcdefghijklmnopqrstuvwxyz'

    for i in range(0, len(group)):
        for char in allchars:
            if group[i].find(char) >= 0:
                if count[allchars.find(char)] < 1:
                    count[allchars.find(char)]  += 1
    
    for i in count:
        total_count += i

    return total_count

def count_shared_answers(group):
    count = [0] * 26
    total_count = 0

    allchars = 'abcdefghijklmnopqrstuvwxyz'

    for i in range(0, len(group)):
        for char in allchars:
            if group[i].find(char) >= 0:
                count[allchars.find(char)]  += 1

    for i in count:
        if i != 0 and i == len(group):
            total_count += 1

    return total_count

if __name__ == "__main__":
    values = read_input()

    all_groups = split_into_groups(values)

    # part 1
    total = 0
    
    for group in all_groups:
        total += count_unique_answers(group)
    
    print(total)

    # part 2
    total = 0

    for group in all_groups:
        total += count_shared_answers(group)
    
    print(total)
