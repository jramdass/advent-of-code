import re
from collections import Counter

def read_input():
    inputs = []

    input_file = open("input")
    for line in input_file:
        inputs.append(line.strip('\n'))

    return inputs

def connect_lines(inputs):
    x_1 = 0
    x_2 = 0
    y_1 = 0
    y_2 = 0

    points = []

    for pair in inputs:
        x_1, y_1, x_2, y_2 = re.findall(r'\d{2,3}', pair)
        x_1 = int(x_1)
        x_2 = int(x_2)
        y_1 = int(y_1)
        y_2 = int(y_2)

        mod_x = 1
        mod_y = 1
        if x_1 > x_2:
            mod_x = -1
        if y_1 > y_2:
            mod_y = -1

        if x_1 == x_2:
            for j in range(y_1, y_2+mod_y, mod_y):
                points.append((x_1, j))
        elif y_1 == y_2:
            for i in range(x_1, x_2+mod_x, mod_x):
                points.append((i, y_1))
        # comment else block for part 1 solution
        else:
            for i in range(x_1, x_2+mod_x, mod_x):
                points.append((i, y_1))
                if mod_y == -1:
                    y_1 -= 1
                else:
                    y_1 += 1

    return points

def count_multiple_points(points):
    my_dict = dict(Counter(points))

    count = 0
    for x, y in my_dict:
        if my_dict[(x, y)] >= 2:
            count += 1

    return count


if __name__ == "__main__":
    values = read_input()

    # part 1 and 2 - comment else in connect_lines()
    # for part 1 solution
    all_points = connect_lines(values)

    duplicate_points = count_multiple_points(all_points)
    print(duplicate_points)
