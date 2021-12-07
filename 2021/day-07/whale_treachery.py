import re

def read_input():
    inputs = []

    input_file = open("input")
    for line in input_file:
        inputs.append(line.strip('\n'))

    return inputs

def min_horizontal_constant(positions):
    all_distances = {}

    for pos in range(len(positions)):
        distance = 0
        for _, val in enumerate(positions):
            distance += abs(val - pos)
        all_distances[pos] = distance

    min_key = min(all_distances, key=all_distances.get)
    return all_distances.get(min_key)

def min_horizontal_linear(positions):
    all_distances = {}

    for pos in range(max(positions)+1):
        distance = 0
        for _, val in enumerate(positions):
            temp = abs(val - pos)
            distance += int((temp*(temp+1))/2)
        all_distances[pos] = distance

    min_key = min(all_distances, key=all_distances.get)
    return all_distances.get(min_key)

if __name__ == "__main__":
    values = read_input()

    values = re.findall(r'\d{1,4}', values[0])
    for count, value in enumerate(values):
        values[count] = int(value)

    # part 1
    least_fuel = min_horizontal_constant(values)
    print(least_fuel)

    # part 2
    least_fuel = min_horizontal_linear(values)
    print(least_fuel)
