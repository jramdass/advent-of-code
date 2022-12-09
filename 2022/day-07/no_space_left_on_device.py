def read_input():
    input_values = []

    file = open("input")
    for line in file:
        input_values.append(line.strip('\n'))

    return input_values

class Node:
    def __init__(self, name, parent):
        self.value = 0
        self.children = []
        self.name = name
        self.parent = parent
        self.child_index = -1

    def append_child(self, child):
        self.children.append(child)

    def update_value(self, new_value):
        self.value += new_value

    def get_value(self):
        return self.value

    def get_children(self):
        return self.children

    def get_parent(self):
        return self.parent

    def update_index(self):
        self.child_index += 1

def calculate_sum(parent_node):
    node_sum = 0

    children = parent_node.get_children()
    for child in children:
        node_sum += child.get_value()
        node_sum += calculate_sum(child)

    return node_sum

if __name__ == "__main__":
    values = read_input()

    tree = []

    for c,v in enumerate(values):
        if v.rfind("$") >= 0:
            values[c] = v[2:]

    # part 1

    initial_node = True
    for value in values:
        if value[0:2] == 'cd' and value.rfind('..') < 0:
            if not initial_node:
                temp = new_node.get_children()
                total_children = len(new_node.get_children())
                new_node.update_index()
                new_node = temp[new_node.child_index]
                total_children -= 1

            if initial_node:
                new_node = Node(value.split(' ')[1], None)
                tree.append(new_node)
                initial_node = False

        if value.rfind('..') >= 0:
            new_node = new_node.get_parent()

        if value[0:3] == ('dir'):
            child_node = Node(value.split(' ')[1], new_node)
            new_node.append_child(child_node)
            tree.append(child_node)

        if value[0].isdigit():
            new_node.update_value(int(value.split(' ')[0]))

    for node in tree:
        node.update_value(calculate_sum(node))

    total = 0
    for node in tree:
        if node.get_value() <= 100000:
            total += node.get_value()
    print(total)

    # part 2
    MAX_SPACE = 70000000
    REQUIRED_SPACE = 30000000
    used_space = MAX_SPACE - tree[0].value
    free_space = REQUIRED_SPACE - used_space

    folder_space = []
    for node in tree:
        if node.value > free_space:
            folder_space.append(node.value)

    print(min(folder_space))
