def read_input():
    values = []

    input = open("input")
    for line in input:
        values.append(line.strip('\n'))

    return values

def check_increasing(values):
    increasing = 0
    for i in range(len(values)):
        if int(values[i]) > int(values[i-1]):
            increasing += 1

    return increasing

def check_increasing_windows(values):
    increasing = 0
    previous_sum = 0

    for i in range(len(values)):
        if (i+3) < len(values):
            if int(values[i]) + int(values[i+1]) + int(values[i+2]) > previous_sum:
                increasing += 1
            previous_sum = int(values[i]) + int(values[i+1]) + int(values[i+2])
        else:
            break

    return increasing

if __name__ == "__main__":
    values = read_input()

    # part 1
    print(check_increasing(values))

    # part 2
    print(check_increasing_windows(values))
