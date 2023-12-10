from dataclasses import dataclass, field
from enum import IntEnum


class Direction(IntEnum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


@dataclass
class AreaCell:
    inner: bool = False


@dataclass
class LoopCell:
    left: bool = False
    right: bool = False
    up: bool = False
    down: bool = False
    is_in_loop = False


@dataclass
class GridMap:
    width: int
    height: int
    grid: dict[(int, int), LoopCell] = field(default_factory=dict)
    area: dict[(int, int), AreaCell] = field(default_factory=dict)
    start: tuple[int, int] = (-1, -1)

    def print_grid(self):
        gmap = [['░'] * self.width for _ in range(self.height)]
        for (x, y), cell in self.grid.items():
            if (x, y) == self.start:
                gmap[y][x] = '╬'
            elif cell.left and cell.right:
                gmap[y][x] = '─'
            elif cell.up and cell.down:
                gmap[y][x] = '│'
            elif cell.up and cell.right:
                gmap[y][x] = '└'
            elif cell.down and cell.right:
                gmap[y][x] = '┌'
            elif cell.up and cell.left:
                gmap[y][x] = '┘'
            elif cell.down and cell.left:
                gmap[y][x] = '┐'
        for (x, y), cell in self.area.items():
            if cell.inner:
                gmap[y][x] = '█'

        for line in gmap:
            print(''.join(line))

    def find_loop(self):
        self.grid[self.start].is_in_loop = True
        current_pos = self.start
        direction = None
        # Find first direction
        if self.grid[current_pos].right:
            current_pos = (current_pos[0] + 1, current_pos[1])
            self.grid[current_pos].is_in_loop = True
            direction = Direction.RIGHT
        elif self.grid[current_pos].left:
            current_pos = (current_pos[0] - 1, current_pos[1])
            self.grid[current_pos].is_in_loop = True
            direction = Direction.LEFT
        elif self.grid[current_pos].down:
            current_pos = (current_pos[0], current_pos[1] + 1)
            self.grid[current_pos].is_in_loop = True
            direction = Direction.DOWN
        elif self.grid[current_pos].up:
            current_pos = (current_pos[0], current_pos[1] - 1)
            self.grid[current_pos].is_in_loop = True
            direction = Direction.UP

        while current_pos != self.start:
            cell = self.grid[current_pos]
            if cell.right and direction != Direction.LEFT:
                current_pos = (current_pos[0] + 1, current_pos[1])
                self.grid[current_pos].is_in_loop = True
                direction = Direction.RIGHT
            elif cell.left and direction != Direction.RIGHT:
                current_pos = (current_pos[0] - 1, current_pos[1])
                self.grid[current_pos].is_in_loop = True
                direction = Direction.LEFT
            elif cell.down and direction != Direction.UP:
                current_pos = (current_pos[0], current_pos[1] + 1)
                self.grid[current_pos].is_in_loop = True
                direction = Direction.DOWN
            elif cell.up and direction != Direction.DOWN:
                current_pos = (current_pos[0], current_pos[1] - 1)
                self.grid[current_pos].is_in_loop = True
                direction = Direction.UP

        self.grid = {k: v for k, v in self.grid.items() if v.is_in_loop}

    def find_inner_area(self):
        for y in range(self.height):
            inner = False
            x = 0
            while x < self.width:
                if (x, y) in self.grid:
                    if self.grid[(x, y)].up and self.grid[(x, y)].down:
                        inner = not inner
                    elif self.grid[(x, y)].up:
                        while self.grid[(x, y)].right:
                            x += 1
                        if self.grid[(x, y)].down:
                            inner = not inner
                    elif self.grid[(x, y)].down:
                        while self.grid[(x, y)].right:
                            x += 1
                        if self.grid[(x, y)].up:
                            inner = not inner
                else:
                    self.area[(x, y)] = AreaCell(inner=inner)
                x += 1
        self.area = {k: v for k, v in self.area.items() if v.inner}
        return len(self.area)


def parse_input(lines):
    grid_map: GridMap = GridMap(len(lines[0]), len(lines))
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            match char:
                case '-':
                    grid_map.grid[(x, y)] = LoopCell(left=True, right=True)
                case '|':
                    grid_map.grid[(x, y)] = LoopCell(up=True, down=True)
                case '7':
                    grid_map.grid[(x, y)] = LoopCell(left=True, down=True)
                case 'L':
                    grid_map.grid[(x, y)] = LoopCell(right=True, up=True)
                case 'J':
                    grid_map.grid[(x, y)] = LoopCell(left=True, up=True)
                case 'F':
                    grid_map.grid[(x, y)] = LoopCell(right=True, down=True)
                case 'S':
                    grid_map.start = (x, y)
    start_x, start_y = grid_map.start
    grid_map.grid[grid_map.start] = LoopCell(
        left=(start_x - 1, start_y) in grid_map.grid and grid_map.grid[(start_x - 1, start_y)].right,
        right=(start_x + 1, start_y) in grid_map.grid and grid_map.grid[(start_x + 1, start_y)].left,
        up=(start_x, start_y - 1) in grid_map.grid and grid_map.grid[(start_x, start_y - 1)].down,
        down=(start_x, start_y + 1) in grid_map.grid and grid_map.grid[(start_x, start_y + 1)].up)
    return grid_map


def main():
    with open("input.txt", 'r') as f:
        lines = f.read().splitlines()

    grid_map = parse_input(lines)
    grid_map.find_loop()
    inner_tiles = grid_map.find_inner_area()
    grid_map.print_grid()
    print(inner_tiles)


if __name__ == "__main__":
    main()
