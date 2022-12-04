def read_input():
    input_values = []

    file = open("input")
    for line in file:
        input_values.append(line.strip('\n'))

    return input_values


if __name__ == "__main__":
    values = read_input()

    # part 1
    pairs = []

    for row in values:
        pairs.append(row)

    matches = 0
    for pair in pairs:
        pair1, pair2 = pair.split(',')

        begin1, end1 = pair1.split('-')
        begin1 = int(begin1)
        end1 = int(end1)

        begin2, end2 = pair2.split('-')
        begin2 = int(begin2)
        end2 = int(end2)

        if begin2 >= begin1 and end2 <= end1:
            matches += 1
        elif begin1 >= begin2 and end1 <= end2:
            matches += 1

    print(matches)

    # part 2
    matches = 0
    for pair in pairs:
        pair1, pair2 = pair.split(',')

        begin1, end1 = pair1.split('-')
        begin1 = int(begin1)
        end1 = int(end1)

        begin2, end2 = pair2.split('-')
        begin2 = int(begin2)
        end2 = int(end2)

        if end2 >= begin1 >= begin2 or begin2 <= end1 <= end2:
            matches +=1
        elif end1 >= begin2 >= begin1 or begin1 <= end2 <= end1:
            matches +=1

    print(matches)
