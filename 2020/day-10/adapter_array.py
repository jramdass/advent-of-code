def read_input():
    values = []

    input = open("input")
    for line in input:
        values.append(line.strip('\n'))

    return values

def use_adapters(adapters, max_joltage):
    num_1_higher = 0
    num_3_higher = 0

    adapters = sorted(adapters)

    i = 0
    while i < max_joltage-3:
        for adapter in adapters:
            if adapter == i+1:
                num_1_higher += 1
                
                adapters.remove(adapter)
                i += 1
                break

            elif adapter == i+3:
                num_3_higher += 1
                
                adapters.remove(adapter)
                i += 3
                break

    return num_1_higher * (num_3_higher+1)

if __name__ == "__main__":
    values = read_input()
    
    # part 1
    adapters = []
    for value in values:
        adapters.append(int(value))

    max_joltage = max(adapters)+3

    answer = use_adapters(adapters, max_joltage)

    print(answer)