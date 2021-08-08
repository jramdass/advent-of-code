from math import sin, cos, radians

def read_input():
    values = []

    input = open("input")
    for line in input:
        values.append(line.strip('\n'))

    return values

def change_direction(starting_direction, rotation, rotation_direction):
    if(rotation_direction == 'L'):
        rotation *= -1

    return (starting_direction[0] * round(cos(radians(rotation))) - starting_direction[1] * round(sin(radians(rotation))), 
            starting_direction[0] * round(sin(radians(rotation))) + starting_direction[1] * round(cos(radians(rotation))))

def change_position(initial_position, direction, unit):
    if(direction == 'N'):
        initial_position[1] -= unit
    elif(direction == 'E'):
        initial_position[0] += unit
    elif(direction == 'S'):
        initial_position[1] += unit
    elif(direction == 'W'):
        initial_position[0] -= unit

    return initial_position

def move_forward(initial_position, initial_direction, unit):
    if(initial_direction == (0,-1)):
        change_position(initial_position, 'N', unit)
    elif(initial_direction == (1,0)):
        change_position(initial_position, 'E', unit)
    elif(initial_direction == (0,1)):
        change_position(initial_position, 'S', unit)
    elif(initial_direction == (-1,0)):
        change_position(initial_position, 'W', unit)

    return initial_position

def calculate_distance(position):
    return abs(position[0]) + abs(position[1])

def move_toward_waypoint(initial_position, waypoint_position, unit):
    x_unit = waypoint_position[0] * unit
    y_unit = waypoint_position[1] * unit

    if x_unit > 0:
        change_position(initial_position, 'E', abs(x_unit))  
    else:
        change_position(initial_position, 'W', abs(x_unit))  

    if y_unit > 0:
        change_position(initial_position, 'S', abs(y_unit))
    else:
        change_position(initial_position, 'N', abs(y_unit))


if __name__ == "__main__":
    values = read_input()
    
    # part 1
    initial_position = [0, 0]
    initial_direction = (1, 0)

    for line in values:
        if(line[0] == 'F'):
            move_forward(initial_position, initial_direction, int(line[1:]))
        elif(line[0] in ('N', 'E', 'S', 'W')):
            change_position(initial_position, line[0], int(line[1:]))
        elif(line[0] in ('R', 'L')):
            initial_direction = change_direction(initial_direction, int(line[1:]), line[0])

    print(calculate_distance(initial_position))

    # part 2
    initial_position = [0, 0]
    waypoint_position = [10, -1]

    for line in values:
        if(line[0] == 'F'):
            move_toward_waypoint(initial_position, waypoint_position, int(line[1:]))

        elif(line[0] in ('N', 'E', 'S', 'W')):
            change_position(waypoint_position, line[0], int(line[1:]))

        elif(line[0] in ('R', 'L')):
            temp = change_direction(waypoint_position, int(line[1:]), line[0])
            waypoint_position[0] = temp[0]
            waypoint_position[1] = temp[1]

    print(calculate_distance(initial_position))
    