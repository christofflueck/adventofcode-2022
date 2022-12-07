from run_util import run_puzzle


class Dir:

    def __init__(self, parent, name) -> None:
        super().__init__()
        self.dirs = {}
        self.files = {}
        self.parent = parent
        self.name = name

    def __str__(self) -> str:
        if self.parent:
            return str(self.parent) + self.name + '/'
        return self.name

    def get_size(self):
        return sum([dir.get_size() for dir in self.dirs.values()]) + sum(self.files.values())


def read_tree(data):
    commands = data.split('\n')
    base = Dir(name='/', parent=None)
    curr_dir = base
    for command in commands:
        if command.startswith('$'):
            args = command[2:].split(' ')
            match args[0]:
                case 'cd':
                    match args[1]:
                        case '/':
                            curr_dir = base
                        case '..':
                            if curr_dir.parent:
                                curr_dir = curr_dir.parent
                        case other:
                            if args[1] not in curr_dir.dirs.keys():
                                new_dir = Dir(parent=curr_dir, name=args[1])
                                curr_dir.dirs[args[1]] = new_dir
                            else:
                                new_dir = curr_dir.dirs[args[1]]
                            curr_dir = new_dir
                case 'ls':
                    pass
                case other:
                    print('Unrecognized command', args[0])
        elif command.startswith('dir'):
            pass
        else:
            size, name = command.split()
            curr_dir.files[name] = int(size)
    return base


def part_a(data):
    base = read_tree(data)
    small_dirs = []

    get_small_dirs(base, small_dirs)

    return sum(small_dir.get_size() for small_dir in small_dirs)


def get_small_dirs(curr_dir, small_dirs):
    for name in curr_dir.dirs:
        child_dir = curr_dir.dirs[name]
        if child_dir.get_size() <= 100000:
            small_dirs.append(child_dir)
        get_small_dirs(child_dir, small_dirs)


def get_all_sizes(curr_dir, dirs):
    dirs.append(curr_dir.get_size())
    for child_dir in curr_dir.dirs.values():
        get_all_sizes(child_dir, dirs)


def part_b(data):
    base = read_tree(data)

    total = 70000000
    free = total - base.get_size()
    required = 30000000

    missing = required - free

    dirs = []
    get_all_sizes(base, dirs)

    current_min = total

    for size in dirs:
        if missing < size < current_min:
            current_min = size

    return current_min


def main():
    examples = [
        ("""$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k""", 95437, 24933642)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()
