import re
from collections import Counter
import itertools

def read_input():
    inputs = []

    input_file = open("input")
    for line in input_file:
        inputs.append(line.strip('\n'))

    return inputs

def simulate_lanternfish(values, days):
    fish_dict = dict(Counter(values))
    for i in range(9):
        if i not in fish_dict:
            fish_dict[i] = None
    fish_dict = dict(sorted(fish_dict.items()))

    for _ in itertools.repeat(None, days):
        for i in fish_dict:
            if fish_dict.get(i) == 0:
                fish_dict[i] = None

        num_0 = find_current_0s(fish_dict)
        if num_0 > 0:
            fish_dict[0] = 0

        subtract_one_day(fish_dict)
        append_8s(fish_dict, num_0)
        reset_0_to_6(fish_dict, num_0)

    total = 0
    for k in fish_dict:
        if fish_dict.get(k) is not None:
            total += fish_dict.get(k)

    return total

def find_current_0s(input_dict):
    num_0 = 0
    if input_dict.get(0) is not None:
        num_0 = input_dict.get(0)
    return num_0

def subtract_one_day(input_dict):
    for i in input_dict:
        if input_dict.get(i) is not None:
            if (i-1) >= 0:
                if input_dict.get(i-1) is None:
                    input_dict[i-1] = input_dict.get(i)
                else:
                    input_dict[i-1] += input_dict.get(i)
            input_dict[i] -= input_dict.get(i)

def append_8s(input_dict, total_0s):
    if total_0s > 0:
        if input_dict.get(8) is None:
            input_dict[8] = total_0s
        else:
            input_dict[8] += total_0s

def reset_0_to_6(input_dict, total_0s):
    if total_0s > 0:
        if input_dict.get(6) is None:
            input_dict[6] = total_0s
        else:
            input_dict[6] += total_0s


if __name__ == "__main__":
    initial_conditions = read_input()
    initial_conditions = re.findall(r'\d{1}', initial_conditions[0])

    for count, _ in enumerate(initial_conditions):
        initial_conditions[count] = int(initial_conditions[count])

    # part 1
    total_fish = simulate_lanternfish(initial_conditions, 80)
    print(total_fish)

    # part 2
    total_fish = simulate_lanternfish(initial_conditions, 256)
    print(total_fish)
