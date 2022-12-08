from itertools import product


PUZZLE_INPUT_FILEPATH = "day8/input.txt"


trees_visible = 0
scenic_score = 0
if __name__ == "__main__":
    data = [ [ *map(int, line.strip()) ] for line in open(PUZZLE_INPUT_FILEPATH).readlines() ]
    rows, cols = len(data), len(data[0])

    for row, col in product(range(rows), range(cols)):
        tree = data[row][col]
        
        # Update the answer for part 1.
        trees_visible += any((
            all(x < tree for x in data[row][:col]),
            all(x < tree for x in data[row][:col:-1]),
            all(x < tree for x in [ x[col] for x in data[:row] ]),
            all(x < tree for x in [ x[col] for x in data[:row:-1] ])
        ))
        
        # Calculate the scenic score for part 2.
        # Why was part 2 so hard compared to part 1?
        if row > 0 and col > 0 and row < rows-1 and col < cols-1:
            up = 0
            for i in range(row-1, -1, -1):
                other_tree = data[i][col]
                if other_tree < tree:
                    up += 1
                else:
                    up += 1
                    break
            down = 0
            for i in range(row+1, rows):
                other_tree = data[i][col]
                if other_tree < tree:
                    down += 1
                else:
                    down += 1
                    break
            left = 0
            for i in range(col-1, -1, -1):
                other_tree = data[row][i]
                if other_tree < tree:
                    left += 1
                else:
                    left += 1
                    break
            right = 0
            for i in range(col+1, cols):
                other_tree = data[row][i]
                if other_tree < tree:
                    right += 1
                else:
                    right += 1
                    break
            score = up * down * left * right
            if score > scenic_score:
                scenic_score = score

    print(trees_visible)
    print(scenic_score)