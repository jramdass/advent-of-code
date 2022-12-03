def read_input():
    input_values = []

    file = open("input")
    for line in file:
        input_values.append(line.strip('\n'))

    return input_values


OUTCOME = {
    ("A", "Y"): "WIN",
    ("B", "Z"): "WIN",
    ("C", "X"): "WIN",
    ("A", "X"): "DRAW",
    ("B", "Y"): "DRAW",
    ("C", "Z"): "DRAW",
    ("A", "Z"): "LOSE",
    ("B", "X"): "LOSE",
    ("C", "Y"): "LOSE"
}

FIXED_MATCH = {
    ("A", "X"): "Z",
    ("A", "Y"): "X",
    ("A", "Z"): "Y",
    ("B", "X"): "X",
    ("B", "Y"): "Y",
    ("B", "Z"): "Z",
    ("C", "X"): "Y",
    ("C", "Y"): "Z",
    ("C", "Z"): "X"
}

ORIGINAL_SCORES = {
    "X": 1,
    "Y": 2,
    "Z": 3,
    "WIN": 6,
    "DRAW": 3,
    "LOSE": 0
}

NEW_SCORES = {
    "X": 0,
    "Y": 3,
    "Z": 6
}

if __name__ == "__main__":
    values = read_input()

    # part 1
    score = 0
    for row in values:
        score += ORIGINAL_SCORES[row[2]]
        choice = OUTCOME[(row[0], row[2])]
        score += ORIGINAL_SCORES[choice]
    print(score)

    # part 2
    score = 0
    for row in values:
        choice = FIXED_MATCH[(row[0], row[2])]
        score += ORIGINAL_SCORES[choice]
        score += NEW_SCORES[row[2]]

    print(score)
