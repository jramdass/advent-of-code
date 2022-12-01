def read_input():
    input_values = []

    file = open("input")
    for line in file:
        input_values.append(line.strip('\n'))

    return input_values


if __name__ == "__main__":
    values = read_input()

    # part 1
    totals = {}
    temp = 0
    index = 0
    for v in values:
        if v != '':
            temp += int(v)
        if v == '':
            totals[index] = temp
            index += 1
            temp = 0

    calories = totals.values()
    print(max(calories))

    # part 2
    sortedTotals = sorted(totals.items(), key=lambda x: -x[1])
    print(sortedTotals[0][1] + sortedTotals[1][1] + sortedTotals[2][1])
