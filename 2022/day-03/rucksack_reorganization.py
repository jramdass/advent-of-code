def read_input():
    input_values = []

    file = open("input")
    for line in file:
        input_values.append(line.strip('\n'))

    return input_values


ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

if __name__ == "__main__":
    values = read_input()

    # part 1
    comp1 = []
    comp2 = []
    for row in values:
        comp1.append(row[0:int(len(row)/2)])
        comp2.append(row[int(len(row)/2):])

    match = []
    for c,v in enumerate(comp1):
        for letter in v:
            if comp2[c].find(letter) >= 0:
                match.append(letter)
                break

    total = 0
    for item in match:
        total += ALPHABET.rfind(item)+1

    print(total)


    # part 2
    comp = []
    index = 0
    for c,v in enumerate(values):
        if c == index+2:
            comp.append((values[c-2], values[c-1], values[c]))
            index += 3

    match = []
    for words in comp:
        for letter in words[0]:
            if words[1].find(letter) >= 0 and words[2].find(letter) >= 0:
                match.append(letter)
                break

    total = 0
    for item in match:
        total += ALPHABET.rfind(item)+1

    print(total)
