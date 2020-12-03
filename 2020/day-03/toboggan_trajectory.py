def read_input():
    values = []

    input = open("input")
    for line in input:
        values.append(line)

    return values

def count_trees(values):
    num_trees = 0
    x_pos = 0
    y_pos = 0
    x_width = len(values[0]) - 1
    y_max = len(values)             

    while(y_pos+1 < y_max):
        x_pos += 3
        if x_pos >= x_width:
            x_pos = x_pos - x_width
        
        y_pos += 1

        if((values[y_pos])[x_pos]  == '#'):
            num_trees += 1

    return num_trees

def count_trees_with_slope(values, slope):
    num_trees = 0
    x_pos = 0
    y_pos = 0
    x_width = len(values[0]) - 1
    y_max = len(values)         

    x_slope = slope[0]
    y_slope = slope[1]   

    while(y_pos+y_slope < y_max):
        x_pos += x_slope
        if x_pos >= x_width:
            x_pos = x_pos - x_width
        
        y_pos += y_slope

        if((values[y_pos])[x_pos]  == '#'):
            num_trees += 1

    return num_trees


if __name__ == "__main__":
    
    values = read_input()

    # part 1
    num_trees = count_trees(values)

    print(num_trees)

    # part 2
    num_trees = 1

    slopes = [(1,1), 
              (3,1), 
              (5,1),
              (7,1),
              (1,2)]
    
    for slope in slopes:
        num_trees *= count_trees_with_slope(values, slope)

    print(num_trees)
