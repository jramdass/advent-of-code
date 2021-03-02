import re

def read_input():
    values = []

    input = open("input")
    for line in input:
        values.append(line)

    return values

def parse_input(values):
    all_ops = []

    for line in values:
        
        op = (re.findall('\w{3}', line)[0], re.findall('[+]\d{1,}|[-]\d{1,}', line)[0])
        all_ops.append(op)

    return all_ops

def process_ops(all_ops):
    acc = 0

    op_visited = []

    for i in range(0, len(all_ops)):
        op_visited.append(0)

    i = 0
    while(1):
        if op_visited[i] > 0:
            break

        op_visited[i] = 1

        if all_ops[i][0] == 'nop':
            i += 1
        elif all_ops[i][0]  == 'acc':
            acc += int(all_ops[i][1])
            i += 1
        else:
            i += int(all_ops[i][1])

    return acc

def fix_op(all_ops):
    for op in all_ops:
        new_ops = all_ops.copy()

        index = all_ops.index(op)
    
        if op[0] == 'nop':
            new_op = ('jmp', op[1])
            new_ops[index] = new_op
        elif op[0] == 'jmp':
            new_op = ('nop', op[1])
            new_ops[index] = new_op
        
        op_visited = []
        for i in range(0, len(all_ops)):
            op_visited.append(0)

        i = 0
        acc = 0

        while(1):
            if op_visited[i] > 0:
                break

            op_visited[i] = 1

            if new_ops[i][0] == 'nop':
                i += 1
            elif new_ops[i][0]  == 'acc':
                acc += int(new_ops[i][1])
                i += 1
            else:
                i += int(new_ops[i][1])

            if i == len(all_ops):
                return acc

    return acc
    

if __name__ == "__main__":
    values = read_input()

    all_ops = parse_input(values)

    # part 1
    acc = process_ops(all_ops)
    print(acc)

    # part 2
    final_op = fix_op(all_ops)
    print(final_op)
