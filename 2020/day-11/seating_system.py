def read_input():
    values = []

    input = open("input")
    for line in input:
        values.append(line.strip('\n'))

    return values

def get_seating_chart(input):
    rows = len(input)
    columns = len(input[0])

    seating_chart = [['' for i in range(columns)] for j in range(rows)]

    for i in range(0, rows):
        for k in range(0, columns):
            seating_chart[i][k] = input[i][k] 

    return seating_chart

def count_occupied_seats(seating_chart):
    occupied_num = 0
    rows = len(seating_chart)
    columns = len(seating_chart[0])

    for i in range(0, rows):
        for k in range(0, columns):
            if seating_chart[i][k] == '#':
                occupied_num += 1

    return occupied_num

def seat_arrivals(seating_chart):
    seating_chart_to_update = seating_chart.copy()

    rows = len(seating_chart_to_update)
    columns = len(seating_chart_to_update[0])

    new_seating_chart = [['' for i in range(columns)] for j in range(rows)]

    for i in range(0, rows):
        for k in range(0, columns):
            if seating_chart_to_update[i][k] == 'L':
                occupied_adjacent_seats = check_adjacent_seats(seating_chart_to_update, i, k)
                if occupied_adjacent_seats == 0:
                    new_seating_chart[i][k] = '#'
                else: 
                    new_seating_chart[i][k] = 'L'
            elif seating_chart_to_update[i][k] == '#':
                occupied_adjacent_seats = check_adjacent_seats(seating_chart_to_update, i, k)
                if occupied_adjacent_seats >= 4:
                    new_seating_chart[i][k] = 'L'
                else:
                    new_seating_chart[i][k] = '#'
            else:
                new_seating_chart[i][k] = '.'     

    return new_seating_chart.copy()

def check_adjacent_seats(seating_chart, i, k):
    occupied_adjacent_seats = 0

    rows = len(seating_chart)
    columns = len(seating_chart[0])

    for row in range(i-1, i+2):
        for col in range(k-1, k+2):
            if row == i and col == k:
                pass
            else:
                if row >= 0 and col >= 0 and row <= rows-1 and col <= columns-1:
                    if seating_chart[row][col] == '#':
                        occupied_adjacent_seats += 1

    return occupied_adjacent_seats

def seat_arrivals_by_line(seating_chart):

    seating_chart_to_update = seating_chart.copy()

    rows = len(seating_chart_to_update)
    columns = len(seating_chart_to_update[0])

    new_seating_chart = [['' for i in range(columns)] for j in range(rows)]

    for i in range(0, rows):
        for k in range(0, columns):
            if seating_chart_to_update[i][k] == 'L':
                occupied_adjacent_seats = check_line_of_seats(seating_chart_to_update, i, k)
                if occupied_adjacent_seats == 0:
                    new_seating_chart[i][k] = '#'
                else: 
                    new_seating_chart[i][k] = 'L'
            elif seating_chart_to_update[i][k] == '#':
                occupied_adjacent_seats = check_line_of_seats(seating_chart_to_update, i, k)
                if occupied_adjacent_seats >= 5:
                    new_seating_chart[i][k] = 'L'
                else:
                    new_seating_chart[i][k] = '#'
            else:
                new_seating_chart[i][k] = '.'     

    return new_seating_chart.copy()

def check_line_of_seats(seating_chart, i, k):
    occupied_adjacent_seats = 0

    rows = len(seating_chart)
    columns = len(seating_chart[0])

    itr = k
    for row in range(i-1, -1, -1):
        itr -= 1
        col = itr
        if row >= 0 and col >= 0:
            if seating_chart[row][col] == 'L':
                break
            if seating_chart[row][col] == '#':
                occupied_adjacent_seats += 1
                break
        else:
            break
    
    for row in range(i-1, -1, -1):
        col = k
        if row >= 0 and col >= 0 and row <= rows-1 and col <= columns-1:
            if seating_chart[row][col] == 'L':
                break
            if seating_chart[row][col] == '#':
                occupied_adjacent_seats += 1
                break
        else:
            break

    itr = k
    for row in range(i-1, -1, -1):
        itr += 1
        col = itr
        
        if row >= 0 and col >= 0 and row <= rows-1 and col <= columns-1:
            if seating_chart[row][col] == 'L':
                break
            if seating_chart[row][col] == '#':
                occupied_adjacent_seats += 1
                break
        else:
            break

    for col in range(k-1, -1, -1):
        row = i
        if row >= 0 and col >= 0 and row <= rows-1 and col <= columns-1:
            if seating_chart[row][col] == 'L':
                break
            if seating_chart[row][col] == '#':
                occupied_adjacent_seats += 1
                break
        else:
            break

    for col in range(k+1, columns):
        row = i
        if row >= 0 and col >= 0 and row <= rows-1 and col <= columns-1:
            if seating_chart[row][col] == 'L':
                break
            if seating_chart[row][col] == '#':
                occupied_adjacent_seats += 1
                break
        else:
            break

    itr = k
    for row in range(i+1, rows):
        itr -= 1
        col = itr
        
        if row >= 0 and col >= 0 and row <= rows-1 and col <= columns-1:
            if seating_chart[row][col] == 'L':
                break
            if seating_chart[row][col] == '#':
                occupied_adjacent_seats += 1
                break
        else:
            break

    for row in range(i+1, rows):
        col = k
        if row >= 0 and col >= 0 and row <= rows-1 and col <= columns-1:
            if seating_chart[row][col] == 'L':
                break
            if seating_chart[row][col] == '#':
                occupied_adjacent_seats += 1
                break
        else:
            break

    itr = k
    for row in range(i+1, rows):
        itr += 1
        col = itr
        if row >= 0 and col >= 0 and row <= rows-1 and col <= columns-1:
            if seating_chart[row][col] == 'L':
                break
            elif seating_chart[row][col] == '#':
                occupied_adjacent_seats += 1
                break
        else:
            break
        if row == rows:
            break
    
    return occupied_adjacent_seats  

def all_seat_arrivals(seating_chart, line=False):
    temp = seating_chart.copy()
    if line:    
        updated_seating_chart = seat_arrivals_by_line(seating_chart)
    else:
        updated_seating_chart = seat_arrivals(seating_chart)
    temp2 = updated_seating_chart.copy()

    if temp != temp2:
        final = all_seat_arrivals(updated_seating_chart.copy(), line)
    else:
        final = temp2.copy()

    return final.copy()

if __name__ == "__main__":
    values = read_input()
    
    seating_chart = get_seating_chart(values)

    final_chart = all_seat_arrivals(seating_chart)
    print(count_occupied_seats(final_chart))

    final_chart = all_seat_arrivals(seating_chart, line=True)
    print(count_occupied_seats(final_chart))
