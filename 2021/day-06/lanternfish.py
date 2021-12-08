import re
from collections import Counter
import itertools

MAX_DAYS = 8

def read_input():
    inputs = []

    input_file = open("input")
    for line in input_file:
        inputs.append(line.strip('\n'))

    return inputs

def simulate_lanternfish(values, days):
    fish_dict = dict(Counter(values))
    for i in range(MAX_DAYS+1):
        if i not in fish_dict:
            fish_dict[i] = 0
    fish_dict = dict(sorted(fish_dict.items()))

    for _ in itertools.repeat(None, days):
        num_0 = fish_dict.get(0)
        fish_dict[0] = 0

        for i in fish_dict:
            if (i-1) >= 0:
                fish_dict[i-1] += fish_dict.get(i)
            fish_dict[i] -= fish_dict.get(i)
        fish_dict[8] += num_0
        fish_dict[6] += num_0

    total = sum(fish_dict.values())

    return total


if __name__ == "__main__":
    initial_conditions = read_input()
    initial_conditions = re.findall(r'\d{1}', initial_conditions[0])
    initial_conditions = [int(x) for x in initial_conditions]

    # part 1
    total_fish = simulate_lanternfish(initial_conditions, 80)
    print(total_fish)

    # part 2
    total_fish = simulate_lanternfish(initial_conditions, 256)
    print(total_fish)
