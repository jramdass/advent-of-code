def read_input():
    inputs = []

    input_file = open("input")
    for line in input_file:
        inputs.append(line.strip('\n'))

    return inputs

def course_position(commands):
    horizontal = 0
    depth = 0

    for line in commands:
        if line[0] == 'f':
            horizontal += int(line[-1])
        elif line[0] == 'u':
            depth += int(line[-1])
        else:
            depth -= int(line[-1])

    return horizontal* depth

def course_position_with_aim(commands):
    horizontal = 0
    aim = 0
    depth = 0

    for line in commands:
        if line[0] == 'f':
            horizontal += int(line[-1])
            depth += aim*int(line[-1])
        elif line[0] == 'u':
            aim += int(line[-1])
        else:
            aim -= int(line[-1])

    return horizontal*depth

if __name__ == "__main__":
    values = read_input()

    # part 1
    print(course_position(values))

    # part 2
    print(course_position_with_aim(values))
    