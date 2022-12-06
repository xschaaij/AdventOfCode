PUZZLE_INPUT_FILEPATH = "day6/input.txt"


if __name__ == "__main__":
    data = open(PUZZLE_INPUT_FILEPATH).read()
    
    # Part 1
    for i in range(0, len(data)-4):
        if len(set(data[i:i+4])) == 4:
            print(i+4)
            break
    
    # Part 2
    for i in range(0, len(data)-14):
        if len(set(data[i:i+14])) == 14:
            print(i+14)
            break
    