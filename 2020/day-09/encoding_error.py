def read_input():
    values = []

    input = open("input")
    for line in input:
        values.append(line)

    return values

def find_invalid_number(values, window=5):
    break_num = 0
    for i in range(1, window):
        break_num += i
    
    iteration = 0
    for i in range(window+iteration, len(values)):
        old_list = values[0+iteration:window+iteration]
        count = 0
        sum_found = False

        for j in range(0, len(old_list)-1):
            for k in range(j+1, len(old_list)):
                if int(values[i]) == int(old_list[j])+int(old_list[k]):
                    sum_found = True
                    break
                else:
                    count += 1
                if count >= break_num:
                    return values[i]

            if sum_found:
                break
        iteration += 1
                   
def find_weakness(values, invalid_value):
    sum = 0
    iteration = 0

    while(1):
        for i in range(iteration, len(values)):
            sum += int(values[i])

            if sum == invalid_value:
                return iteration, i+1
            if sum > invalid_value:
                break
        iteration += 1
        sum = 0


if __name__ == "__main__":
    values = read_input()

    # part 1
    invalid_value = int(find_invalid_number(values, 25))
    print(invalid_value)

    # part 2
    weakness = find_weakness(values, invalid_value)

    new_range = []
    for i in range(weakness[0], weakness[1]):
        new_range.append(values[i])

    answer = int(min(new_range)) + int(max(new_range))
    print(answer)
