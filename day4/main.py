PUZZLE_INPUT_FILEPATH = 'day4/input.txt'


if __name__ == "__main__":
    score1, score2 = 0, 0
    for line in open(PUZZLE_INPUT_FILEPATH):
        a, b = line.strip().split(',')
        a1, a2 = (int(x) for x in a.split('-'))
        b1, b2 = (int(x) for x in b.split('-'))
        score1 += (a1 >= b1 and a2 <= b2) or (b1 >= a1 and b2 <= a2) 
        score2 += (a1 <= b1 <= a2) or (b1 <= a1 <= b2)

    # Part 1
    print(score1)

    # Part 2
    print(score2)