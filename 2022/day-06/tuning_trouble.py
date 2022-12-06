def read_input():
    input_values = []

    file = open("input")
    for line in file:
        input_values.append(line.strip('\n'))

    return input_values


if __name__ == "__main__":
    values = read_input()

    # part 1
    distincts = 4

    values = values[0]
    window = []
    for c,v in enumerate(values):
        if c-distincts-1 > 0:
            window = []
            for i in range(distincts):
                window.append(values[c-i])

            if(len(set(window))) >= distincts:
                print(c+1)
                break

    # part 2
    distincts = 14

    window = []
    for c,v in enumerate(values):
        if c-distincts-1 > 0:
            window = []
            for i in range(distincts):
                window.append(values[c-i])

            if(len(set(window))) >= distincts:
                print(c+1)
                break
