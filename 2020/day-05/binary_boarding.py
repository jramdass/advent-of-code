def read_input():
    values = []

    input = open("input")
    for line in input:
        values.append(line.strip('\n'))
        
    return values

def get_seat_position(value):
    column = (0, 7)
    row = (0, 127)

    for i in range(0, len(value)):
        if value[i] == 'F':
            if value[i+1] != 'B' and value[i+1] != 'F':
                row = row[0]
            else:
                row = (row[0], round((row[1] - row[0]) / 2) + row[0] - 1)
        elif value[i] == 'B':
            if value[i+1] != 'B' and value[i+1] != 'F':
                row = row[1]
            else:
                row = (round((row[1] - row[0])/2 + row[0]), row[1])
        elif value[i] == 'L':
            if i == len(value)-1:
                column = column[0]
            else:
                column = (column[0], round((column[1]-column[0])/2) + column[0] -1)
        elif value[i] == 'R':
            if i == len(value)-1:
                column = column[1]
            else:
                column = (round((column[1]-column[0])/2), column[1])
        else:
            pass
    
    return row, column

def seat_to_boarding_pass(seat):
    
    binary_seat_row = str('{0:07b}'.format(seat[0]))
    binary_seat_col = str('{0:03b}'.format(seat[1]))

    boarding_pass = str()

    for char in binary_seat_row:
        if char == '1':
            boarding_pass = boarding_pass + 'B'
        else:
            boarding_pass = boarding_pass + 'F'
    
    for char in binary_seat_col:
        if char == '1':
            boarding_pass = boarding_pass + 'R'
        else:
            boarding_pass = boarding_pass + 'L'

    return(boarding_pass)

def calculate_seat_number(pair):
    return pair[0] * 8 + pair[1]


if __name__ == "__main__":
    values = read_input()

    # part 1
    seat_positions = []
    seat_ids = []

    seat_position_and_ids = []

    for i in range (0, len(values)):
        seat_positions.append(get_seat_position(values[i]))

    for pos in seat_positions:
        seat_ids.append(calculate_seat_number(pos))
        seat_position_and_ids.append((pos, calculate_seat_number(pos)))

    sorted_seat_ids = sorted(seat_ids)
    print(max(sorted_seat_ids))

    # part 2
    seat_range = []

    for i in range(min(sorted_seat_ids), max(sorted_seat_ids)):
        seat_range.append(i)

    missing_seats = set(seat_range).difference(set(sorted_seat_ids))
    missing_seats = list(missing_seats)

    eligible_seats = []
    for i in range(0, len(missing_seats)-1):
        if missing_seats[i]+1 in sorted_seat_ids:
            if missing_seats[i]-1 in sorted_seat_ids:
                eligible_seats.append(missing_seats[i])

    eligible_seat_positions = []
    
    for seat in eligible_seats:
        for row in range(0, 127):
            for column in range(0, 7):
                if row*8 + column == seat:
                    eligible_seat_positions.append((row, column))

    eligible_boarding_passes = []
    for seat in eligible_seat_positions:
        eligible_boarding_passes.append(seat_to_boarding_pass(seat))

    own_boarding_pass = set(eligible_boarding_passes).difference(set(values))
    own_seat_position = get_seat_position(own_boarding_pass.pop())
    print(calculate_seat_number(own_seat_position))
    