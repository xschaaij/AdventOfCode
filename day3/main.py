PUZZLE_INPUT_FILEPATH = 'day3/input.txt'


if __name__ == "__main__":
    PRIORITIES = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    # Calculation part 1
    score = 0
    for line in open(PUZZLE_INPUT_FILEPATH):
        line = line.strip()
        a, b = line[:len(line)//2], line[len(line)//2:]
        for x in line:
            if x in a and x in b:
                score += PRIORITIES.index(x) + 1
                break
    
    # Answer part 1
    print(score)

    # Calculation part 2
    data = [set(x.strip()) for x in open(PUZZLE_INPUT_FILEPATH).readlines()]
    score = 0
    for a, b, c in zip(data[0::3], data[1::3], data[2::3]):
        for x in PRIORITIES:
            if x in a and x in b and x in c:
                score += PRIORITIES.index(x) + 1

    # Answer part 2
    print(score)