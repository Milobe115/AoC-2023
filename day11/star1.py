import re
from dataclasses import dataclass


@dataclass
class SpaceMap:
    galaxies: list[tuple[int, int]]
    empty_rows: list[int]
    empty_cols: list[int]

    def calc_distances(self):
        score = 0
        for idx, galaxy_1 in enumerate(self.galaxies):
            for galaxy_2 in self.galaxies[idx + 1:]:
                dst = abs(galaxy_1[0] - galaxy_2[0]) + abs(galaxy_1[1] - galaxy_2[1])
                dst += len([row for row in self.empty_rows if
                            min(galaxy_1[0], galaxy_2[0]) < row < max(galaxy_1[0], galaxy_2[0])])
                dst += len([col for col in self.empty_cols if
                            min(galaxy_1[1], galaxy_2[1]) < col < max(galaxy_1[1], galaxy_2[1])])
                score += dst
        return score


def parse_map(lines: list[str]) -> SpaceMap:
    galaxies = []
    empty_rows = []
    empty_cols = []

    for row, line in enumerate(lines):
        if set(line) == {"."}:
            empty_rows.append(row)
            continue
        for col, char in enumerate(line):
            if char == "#":
                galaxies.append((row, col))

    for col in range(len(lines[0])):
        if set([line[col] for line in lines]) == {"."}:
            empty_cols.append(col)

    return SpaceMap(galaxies, empty_rows, empty_cols)


def main():
    with open("input.txt", 'r') as f:
        lines = f.read().splitlines()

    space_map = parse_map(lines)
    score = space_map.calc_distances()

    print(f"Score: {score}")


if __name__ == "__main__":
    main()
