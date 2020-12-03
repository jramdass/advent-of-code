def read_input():
    values = []

    input = open("input")
    for line in input:
        values.append(int(line))

    return values

def find_sum_two_operators(values):
    for i in values:
        for j in values:
            if i+j == 2020:
                return i*j

def find_sum_three_operators(values):
    for i in values:
        for j in values:
            for k in values:
                if i+j+k == 2020:
                    return i*j*k


if __name__ == "__main__":
    values = read_input()

    # part 1
    result = find_sum_two_operators(values)
    print(result)

    # part 2
    result = find_sum_three_operators(values)
    print(result)