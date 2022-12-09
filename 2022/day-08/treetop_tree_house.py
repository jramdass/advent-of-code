def read_input():
    input_values = []

    file = open("input")
    for line in file:
        input_values.append(line.strip('\n'))

    return input_values


if __name__ == "__main__":
    values = read_input()

    length = len(values[0])
    height = len(values)
    trees = [[0 for x in range(length)] for y in range(height)]

    for i in range(length):
        for j in range(height):
            trees[i][j] = values[j][i]

    # part 1
    total = 0
    view_blocked = {}
    for j in range(1, height-1):
        for i in range(1, length-1):
            view_blocked["N"] = False
            view_blocked["E"] = False
            view_blocked["S"] = False
            view_blocked["W"] = False

            # looking north
            k = j - 1
            while k >= 0:
                if trees[i][k] >= trees[i][j]:
                    view_blocked["N"] = True
                    break
                k -= 1

            # looking east
            k = i + 1
            while k <= length-1:
                if trees[k][j] >= trees[i][j]:
                    view_blocked["E"] = True
                    break
                k += 1

            # looking south
            k = j + 1
            while k <= height-1:
                if trees[i][k] >= trees[i][j]:
                    view_blocked["S"] = True
                    break
                k += 1

            # looking west
            k = i - 1
            while k >= 0:
                if trees[k][j] >= trees[i][j]:
                    view_blocked["W"] = True
                    break
                k -= 1

            if (not view_blocked["N"] or not view_blocked["E"] or
            not view_blocked["S"] or not view_blocked["W"]):
                total += 1

    total = total + length*2 + (height-2) *2
    print(total)

    # part 2
    max_score = 0
    view_blocked = {}
    for j in range(1, height-1):
        for i in range(1, length-1):
            score =  [0,0,0,0]
            tree_total_score = 0

            view_blocked["N"] = False
            view_blocked["E"] = False
            view_blocked["S"] = False
            view_blocked["W"] = False

            # looking north
            k = j-1
            while k >= 0:
                score[0] += 1
                if trees[i][k] >= trees[i][j]:
                    view_blocked["N"] = True
                    break
                k -= 1

            # looking east
            k = i + 1
            while k <= length-1:
                score[1] += 1
                if trees[k][j] >= trees[i][j]:
                    view_blocked["E"] = True
                    break
                k += 1

            # looking south
            k = j + 1
            while k <= height-1:
                score[2] += 1
                if trees[i][k] >= trees[i][j]:
                    view_blocked["S"] = True
                    break

                k += 1

            # looking west
            k = i - 1
            while k >= 0:
                score[3] += 1
                if trees[k][j] >= trees[i][j]:
                    view_blocked["W"] = True
                    break

                k -= 1

            tree_total_score = score[0]*score[1]*score[2]*score[3]
            if tree_total_score >= max_score:
                max_score = tree_total_score

    print(max_score)
