PUZZLE_INPUT_FILEPATH = 'day1/input.txt'


class Elf:
    def __init__(self, backpack: list[int]) -> None:
        """An Elf, with a little backpack full of snacks.

        Args:
            backpack (list[int]): The calories contained in the elf's snackpack.
        """
        self.backpack = backpack


if __name__ == "__main__":
    # Read puzzle input, perform cursed one-liner.
    data = sorted([Elf(z) for z in map(lambda x: [int(y) for y in x], [x.splitlines() for x in open(PUZZLE_INPUT_FILEPATH).read().split('\n\n')])], key=lambda x: sum(x.backpack), reverse=True)

    # Answer for part 1
    print('Part 1:', sum(data[0].backpack))

    # Answer for part 2
    print('Part 2:', sum(sum(x.backpack) for x in data[:3]))

    # TODO: Contemplate sins.
