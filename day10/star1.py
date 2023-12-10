from dataclasses import dataclass
from enum import IntEnum


class Direction(IntEnum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


@dataclass
class Cell:
    left: bool = False
    right: bool = False
    up: bool = False
    down: bool = False
    is_in_loop = False


@dataclass
class GridMap:
    width: int
    height: int
    grid: dict[(int, int), Cell]
    start: tuple[int, int] = None

    def print_grid(self):
        gmap = [[' '] * self.width for _ in range(self.height)]
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

    def find_farthest(self):
        current_pos_1 = self.start
        current_pos_2 = self.start
        direction_1 = None
        direction_2 = None
        distance = 1
        # Find first direction
        if self.grid[current_pos_1].right:
            current_pos_1 = (current_pos_1[0] + 1, current_pos_1[1])
            direction_1 = Direction.RIGHT
        elif self.grid[current_pos_1].left:
            current_pos_1 = (current_pos_1[0] - 1, current_pos_1[1])
            direction_1 = Direction.LEFT
        elif self.grid[current_pos_1].down:
            current_pos_1 = (current_pos_1[0], current_pos_1[1] + 1)
            direction_1 = Direction.DOWN
        elif self.grid[current_pos_1].up:
            current_pos_1 = (current_pos_1[0], current_pos_1[1] - 1)
            direction_1 = Direction.UP

        if self.grid[current_pos_2].right and direction_1 != Direction.RIGHT:
            current_pos_2 = (current_pos_2[0] + 1, current_pos_2[1])
            direction_2 = Direction.RIGHT
        elif self.grid[current_pos_2].left and direction_1 != Direction.LEFT:
            current_pos_2 = (current_pos_2[0] - 1, current_pos_2[1])
            direction_2 = Direction.LEFT
        elif self.grid[current_pos_2].down and direction_1 != Direction.DOWN:
            current_pos_2 = (current_pos_2[0], current_pos_2[1] + 1)
            direction_2 = Direction.DOWN
        elif self.grid[current_pos_2].up and direction_1 != Direction.UP:
            current_pos_2 = (current_pos_2[0], current_pos_2[1] - 1)
            direction_2 = Direction.UP

        while current_pos_1 != current_pos_2:
            cell_1 = self.grid[current_pos_1]
            cell_2 = self.grid[current_pos_2]
            if cell_1.right and direction_1 != Direction.LEFT:
                current_pos_1 = (current_pos_1[0] + 1, current_pos_1[1])
                direction_1 = Direction.RIGHT
            elif cell_1.left and direction_1 != Direction.RIGHT:
                current_pos_1 = (current_pos_1[0] - 1, current_pos_1[1])
                direction_1 = Direction.LEFT
            elif cell_1.down and direction_1 != Direction.UP:
                current_pos_1 = (current_pos_1[0], current_pos_1[1] + 1)
                direction_1 = Direction.DOWN
            elif cell_1.up and direction_1 != Direction.DOWN:
                current_pos_1 = (current_pos_1[0], current_pos_1[1] - 1)
                direction_1 = Direction.UP

            if cell_2.right and direction_2 != Direction.LEFT:
                current_pos_2 = (current_pos_2[0] + 1, current_pos_2[1])
                direction_2 = Direction.RIGHT
            elif cell_2.left and direction_2 != Direction.RIGHT:
                current_pos_2 = (current_pos_2[0] - 1, current_pos_2[1])
                direction_2 = Direction.LEFT
            elif cell_2.down and direction_2 != Direction.UP:
                current_pos_2 = (current_pos_2[0], current_pos_2[1] + 1)
                direction_2 = Direction.DOWN
            elif cell_2.up and direction_2 != Direction.DOWN:
                current_pos_2 = (current_pos_2[0], current_pos_2[1] - 1)
                direction_2 = Direction.UP

            distance += 1
        return distance


def parse_input(lines):
    grid_map: GridMap = GridMap(len(lines[0]), len(lines), dict())
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            match char:
                case '-':
                    grid_map.grid[(x, y)] = Cell(left=True, right=True)
                case '|':
                    grid_map.grid[(x, y)] = Cell(up=True, down=True)
                case '7':
                    grid_map.grid[(x, y)] = Cell(left=True, down=True)
                case 'L':
                    grid_map.grid[(x, y)] = Cell(right=True, up=True)
                case 'J':
                    grid_map.grid[(x, y)] = Cell(left=True, up=True)
                case 'F':
                    grid_map.grid[(x, y)] = Cell(right=True, down=True)
                case 'S':
                    grid_map.start = (x, y)
    start_x, start_y = grid_map.start
    grid_map.grid[grid_map.start] = Cell(
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
    dist = grid_map.find_farthest()
    print(dist)


if __name__ == "__main__":
    main()
