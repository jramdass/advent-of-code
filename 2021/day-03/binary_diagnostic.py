def read_input():
    inputs = []

    input_file = open("input")
    for line in input_file:
        inputs.append(line.strip('\n'))

    return inputs

def gamma_rate(inputs):
    new_code = []

    for i in range(WORD_LENGTH):
        total_0s = 0
        total_1s = 0
        for _, value in enumerate(inputs):
            if int(value[i]) == 0:
                total_0s += 1
            else:
                total_1s += 1
        if total_0s > total_1s:
            new_code.append(0)
        else:
            new_code.append(1)

    return new_code

def epsilon_rate(inputs):
    new_code = []

    for i in range(WORD_LENGTH):
        total_0s = 0
        total_1s = 0
        for _, value in enumerate(inputs):
            if int(value[i]) == 0:
                total_0s += 1
            else:
                total_1s += 1
        if total_0s < total_1s:
            new_code.append(0)
        else:
            new_code.append(1)

    return new_code

def convert_to_dec(binary_num):
    dec_value = 0
    for i in range(WORD_LENGTH-1, -1, -1):
        if binary_num[WORD_LENGTH-1-i] == 1:
            dec_value += (2**i)
    return dec_value

def find_o2_rating(inputs, position, current_size):
    total_0s = 0
    total_1s = 0

    if current_size == 1:
        return inputs

    for i in range(current_size):
        if int(inputs[i][position]) == 0:
            total_0s += 1
        else:
            total_1s += 1

    keep_value = 1
    keep_inputs = []
    if total_0s > total_1s:
        keep_value = 0

    for i in range(current_size):
        if int(inputs[i][position]) == keep_value:
            keep_inputs.append(inputs[i])
        else:
            current_size -= 1

    return find_o2_rating(keep_inputs, position+1, current_size)

def find_co2_rating(inputs, position, current_size):
    total_0s = 0
    total_1s = 0

    if current_size == 1:
        return inputs

    for i in range(current_size):
        if int(inputs[i][position]) == 0:
            total_0s += 1
        else:
            total_1s += 1

    keep_value = 0
    keep_inputs = []
    if total_0s > total_1s:
        keep_value = 1

    for i in range(current_size):
        if int(inputs[i][position]) == keep_value:
            keep_inputs.append(inputs[i])
        else:
            current_size -= 1

    return find_co2_rating(keep_inputs, position+1, current_size)


if __name__ == "__main__":
    values = read_input()
    global WORD_LENGTH
    WORD_LENGTH = len(values[0])

    # part 1
    gamma = gamma_rate(values)
    epsilon = epsilon_rate(values)

    dec_gamma = convert_to_dec(gamma)
    dec_epsilon = convert_to_dec(epsilon)
    print(dec_gamma*dec_epsilon)

    # part 2
    o2_rating = find_o2_rating(values, 0, len(values))
    co2_rating = find_co2_rating(values, 0, len(values))

    dec_o2_rating = int(o2_rating[0],2)
    dec_co2_rating = int(co2_rating[0],2)
    print(dec_o2_rating*dec_co2_rating)
