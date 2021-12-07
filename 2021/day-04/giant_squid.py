import re
import itertools

def read_input():
    inputs = []

    input_file = open("input")
    for line in input_file:
        inputs.append(line.strip('\n'))

    return inputs

def extract_tables(inputs):
    tables = []
    table = []

    for line in inputs:
        if line != '':
            row = re.findall(r'[\d]{1,2}', line)
            for entry in row:
                entry = int(entry)
            table.append(row)
        else:
            tables.append(table)
            table = []

    tables.append(table)

    return tables

def play_bingo(input_nums, tables):
    for num, table in itertools.product(input_nums, tables):
        for row in table:
            for i, val in enumerate(row):
                if val == num:
                    row[i] = int(row[i])
                    match_found = check_for_bingo(tables)
                    if match_found:
                        return match_found, num
    return None, None

def check_for_bingo(tables):
    for table in tables:
        count_x = 0
        for row in table:
            for col in row:
                if isinstance(col, int):
                    count_x += 1
                if count_x == 5:
                    return table
            count_x = 0

        transposed = [*zip(*table)]

        count_x = 0
        for row in transposed:
            for col in row:
                if isinstance(col, int):
                    count_x += 1
                if count_x == 5:
                    return table
            count_x = 0

    return False

def find_last_board(input_nums, tables):
    for num, table in itertools.product(input_nums, tables):
        for row in table:
            for i, val in enumerate(row):
                if val == num:
                    if len(tables) == 1:
                        return tables
                    row[i] = int(row[i])
                    match_found = check_for_bingo(tables)
                    if match_found:
                        tables.remove(match_found)
                        return find_last_board(input_nums, tables)
    return None, None

def add_remaining_numbers(board):
    sum_remaining = 0
    for row in board:
        for i in row:
            if isinstance(i, str):
                sum_remaining += int(i)
    return sum_remaining

def convert_matched_nums(board):
    for row in last_board[0]:
        for i, val in enumerate(row):
            if isinstance(val, int):
                row[i] = str(row[i])
    return board

if __name__ == "__main__":
    values = read_input()

    nums = values[0]
    number_call = re.findall(r'[\d]{1,2}', nums)

    all_tables = extract_tables(values[2:])

    # part 1
    winning_board, winning_num = play_bingo(number_call, all_tables)
    remainder = add_remaining_numbers(winning_board)

    print(remainder * int(winning_num))

    # part 2
    last_board = find_last_board(number_call, all_tables)
    last_board = convert_matched_nums(last_board)

    winning_board, winning_num = play_bingo(number_call, last_board)

    remainder = add_remaining_numbers(winning_board)
    print(remainder * int(winning_num))
