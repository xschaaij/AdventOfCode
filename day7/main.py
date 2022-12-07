PUZZLE_INPUT_FILEPATH = "day7/input.txt"


if __name__ == "__main__":
    # Parse data into manageable structure
    data = iter(open(PUZZLE_INPUT_FILEPATH).readlines())
    filesystem = {}
    cur = filesystem
    active = []
    flag_ls = False
    while True:
        try:
            line = next(data)
        except StopIteration:
            break

        match line[:4]:
            case "$ cd":
                # Update active directory list
                flag_ls = False
                dir = line[5:].strip()
                if dir == "..":
                    active.pop()
                else:
                    active.append(dir)
                
                # Set cur variable to current directory
                cur = filesystem
                for x in active:
                    if not x in cur:
                        cur[x] = {}
                    cur = cur[x]

            case "$ ls":
                flag_ls = True
                # print(f"Executing 'ls' on {' > '.join(active)}")
                line = next(data)

        # If the flag has been set, interpret line as output of ls command
        if flag_ls:
            a, b = line.strip().split(' ')
            if a.isdigit():
                # print(f"{b} is a file of size {a}")
                cur[b] = int(a)
            else:
                # print(f"{b} is a folder.")
                cur[b] = {}
    
    # Go through a folder and sum the sizes of the items inside it
    def get_folder_size(folder: dict):
        folder_size = 0
        for v in folder.values():
            if isinstance(v, int):
                folder_size += v
            else:
                folder_size += get_folder_size(v)
        return folder_size

    # Get sizes of all folders in filesystem.
    def get_all_sizes(folder: dict):
        for v in folder.values():
            if isinstance(v, dict):
                yield get_folder_size(v)
                yield from get_all_sizes(v)

    # Used for both parts
    sizes = list(get_all_sizes(filesystem))

    # Answer part 1
    print(sum(x for x in sizes if x < 100000))

    # Answer part 2
    needed = 30000000 - (70000000 - max(sizes))
    print(min(x for x in sizes if x >= needed))
