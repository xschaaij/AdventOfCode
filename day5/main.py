PUZZLE_INPUT_FILEPATH = 'day5/input.txt'


if __name__ == "__main__":
    stack, ops = (x.splitlines() for x in open(PUZZLE_INPUT_FILEPATH).read().split('\n\n'))
    _range = range(int(stack.pop()[-2]))
    stacks1 = [[] for _ in _range]
    stacks2 = [[] for _ in _range]

    for line in stack:
        for e, x in enumerate(line[1::4]):
            if x.isspace():
                continue
            stacks1[e].append(x)
            stacks2[e].append(x)

    for op in ops:
        amt, src, dst = [int(x) for x in op.replace('move ', '').replace('from ', '').replace('to ', '').strip().split(' ')]
        grab1 = stacks1[src-1][:amt]
        grab2 = stacks2[src-1][:amt]
        grab1.reverse()
        del stacks1[src-1][:amt]
        del stacks2[src-1][:amt]
        stacks1[dst-1][:0] = grab1
        stacks2[dst-1][:0] = grab2
    
    print('1', ''.join([x[0] for x in stacks1]))
    print('2', ''.join([x[0] for x in stacks2]))