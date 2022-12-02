PUZZLE_INPUT_FILEPATH = 'day2/input.txt'


if __name__ == "__main__":
    score_pt1, score_pt2 = 0, 0
    for line in open(PUZZLE_INPUT_FILEPATH):
        match line.strip():
            case 'B X':
                score_pt1 += 1
                score_pt2 += 1
            case 'C Y':
                score_pt1 += 2
                score_pt2 += 6
            case 'A Z':
                score_pt1 += 3
                score_pt2 += 8
            case 'A X':
                score_pt1 += 4
                score_pt2 += 3
            case 'B Y':
                score_pt1 += 5
                score_pt2 += 5
            case 'C Z':
                score_pt1 += 6
                score_pt2 += 7
            case 'C X':
                score_pt1 += 7
                score_pt2 += 2
            case 'A Y':
                score_pt1 += 8
                score_pt2 += 4
            case 'B Z':
                score_pt1 += 9
                score_pt2 += 9
    
    # Answer part 1
    print(score_pt1)

    # Answer part 2
    print(score_pt2)