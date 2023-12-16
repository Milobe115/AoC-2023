from dataclasses import dataclass
from enum import Enum


class Direction(Enum):
    NORTH = (0, -1)
    EAST = (1, 0)
    SOUTH = (0, 1)
    WEST = (-1, 0)


@dataclass
class Beam:
    x: int
    y: int
    dir: Direction
    is_active: bool = True

    def move(self):
        self.x += self.dir.value[0]
        self.y += self.dir.value[1]


def print_energized_cells(energized_cells: dict[tuple[int, int], list[Direction]], width: int, height: int):
    grid = [[' ' for _ in range(width)] for _ in range(height)]
    for cell in energized_cells:
        grid[cell[1]][cell[0]] = '#'
    print('\n'.join([''.join(['{:1}'.format(item) for item in row]) for row in grid]))


def main():
    with open("input.txt", 'r') as f:
        lines = f.read().splitlines()

    energized_cells: dict[tuple[int, int], list[Direction]] = dict()
    beams = [Beam(0, 0, Direction.EAST)]
    while len(beams) > 0:
        beam = beams.pop()
        while beam.is_active:
            if beam.x < 0 or beam.y < 0 or beam.x >= len(lines[0]) or beam.y >= len(lines):
                beam.is_active = False
            else:
                if (beam.x, beam.y) in energized_cells:
                    if beam.dir in energized_cells[(beam.x, beam.y)]:
                        beam.is_active = False
                    else:
                        energized_cells[(beam.x, beam.y)].append(beam.dir)
                else:
                    energized_cells[(beam.x, beam.y)] = [beam.dir]

                if lines[beam.y][beam.x] == '.':
                    beam.move()
                elif lines[beam.y][beam.x] == '/':
                    if beam.dir == Direction.NORTH:
                        beam.dir = Direction.EAST
                    elif beam.dir == Direction.EAST:
                        beam.dir = Direction.NORTH
                    elif beam.dir == Direction.SOUTH:
                        beam.dir = Direction.WEST
                    elif beam.dir == Direction.WEST:
                        beam.dir = Direction.SOUTH
                    beam.move()
                elif lines[beam.y][beam.x] == '\\':
                    if beam.dir == Direction.NORTH:
                        beam.dir = Direction.WEST
                    elif beam.dir == Direction.EAST:
                        beam.dir = Direction.SOUTH
                    elif beam.dir == Direction.SOUTH:
                        beam.dir = Direction.EAST
                    elif beam.dir == Direction.WEST:
                        beam.dir = Direction.NORTH
                    beam.move()
                elif lines[beam.y][beam.x] == '|':
                    if beam.dir == Direction.NORTH or beam.dir == Direction.SOUTH:
                        beam.move()
                    if beam.dir == Direction.EAST or beam.dir == Direction.WEST:
                        beams.append(Beam(beam.x, beam.y - 1, Direction.NORTH))
                        beams.append(Beam(beam.x, beam.y + 1, Direction.SOUTH))
                        beam.is_active = False
                elif lines[beam.y][beam.x] == '-':
                    if beam.dir == Direction.EAST or beam.dir == Direction.WEST:
                        beam.move()
                    if beam.dir == Direction.NORTH or beam.dir == Direction.SOUTH:
                        beams.append(Beam(beam.x + 1, beam.y, Direction.EAST))
                        beams.append(Beam(beam.x - 1, beam.y, Direction.WEST))
                        beam.is_active = False
    print(len(energized_cells))


if __name__ == "__main__":
    main()
