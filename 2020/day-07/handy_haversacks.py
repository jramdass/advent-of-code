import re

def read_input():
    values = []

    input = open("input")
    for line in input:
        values.append(line)

    return values

def parse_input(values):
    all_bags = []
    bag = {}

    for line in values:
        
        bag['type'] = line[:line.find('bag')-1]
        line = line[line.find('bag'):]

        all_contained_bags = re.findall('\d', line)
        bag['contains'] = {}
        
        bag_list = re.findall('\s\w[a-z]{1,}\s\w[a-z]{1,},|\s\w[a-z]{1,}\s\w[a-z]{1,}.', line)

        i = 0
        for found_bag in all_contained_bags: 
            bag['contains'][bag_list[i].strip(' ')] = found_bag
            i += 1

        all_bags.append(bag)
        bag = {}

    return all_bags

def count_shiny_bags(bag, all_bags):
    if 'contains' in bag:
        for k,v in bag['contains'].items():
            if k == 'shiny gold':
                return 1
            else:
                if bag_lookup(k, all_bags):
                    new_total = count_shiny_bags(bag_lookup(k, all_bags), all_bags)
                    if new_total > 0:
                        return 1

    return 0

def count_total_bags(bag, all_bags):
    total = 1

    for k,v in bag['contains'].items():

        if bag_lookup(k, all_bags):
            num = count_total_bags(bag_lookup(k, all_bags), all_bags)
            total += num  * int(v)

    return total

def bag_lookup(bag_type, all_bags):
    for i in range(0, len(all_bags)):
        if bag_type == all_bags[i]['type']:
            return all_bags[i]

if __name__ == "__main__":
    values = read_input()

    all_bags = parse_input(values)

    # part 1
    total = 0 

    i = 0 
    for bag in all_bags:
        total += count_shiny_bags(bag, all_bags)
        i+=1

    print(total)

    # part 2
    total = 0 

    i = 0
    for bag in all_bags:
        if bag['type'] == 'shiny gold':
            total = count_total_bags(bag, all_bags)
            break
        i+=1
            
    print(total-1)
