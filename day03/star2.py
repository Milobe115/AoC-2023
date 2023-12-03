import operator
import re
from dataclasses import dataclass
from functools import reduce


@dataclass
class Number:
    line: int
    value: int
    start: int
    end: int

    def __init__(self, line: int = 0, value: int = 0, start: int = 0, end: int = 0):
        self.line = line
        self.value = value
        self.start = start
        self.end = end


@dataclass
class Gear:
    line: int
    col: int
    numbers: list[int]

    def __init__(self, line: int = 0, col: int = 0):
        self.line = line
        self.col = col
        self.numbers = []


def extract_numbers(lines: list[str]) -> list[Number]:
    numbers = []
    for line in range(len(lines)):
        for match in re.finditer(r"(\d+)", lines[line]):
            number = Number(line, int(match.group()), match.start(), match.end() - 1)
            numbers.append(number)
    return numbers


def extract_gears(lines: list[str]) -> list[Gear]:
    gears = []
    for line in range(len(lines)):
        for match in re.finditer(r"(\*)", lines[line]):
            gear = Gear(line, match.start())
            gears.append(gear)
    return gears


def main():
    with open("./input.txt", "r") as f:
        lines = list(map(lambda x: x.strip(), f.readlines()))
    numbers = extract_numbers(lines)
    gears = extract_gears(lines)

    ratios_sum = 0

    for number in numbers:
        for gear in gears:
            if number.line - 1 <= gear.line <= number.line + 1 and number.start - 1 <= gear.col <= number.end + 1:
                gear.numbers.append(number.value)

    ratios_sum = sum([reduce(operator.mul, gear.numbers, 1) for gear in gears if len(gear.numbers) >= 2])

    print(f"Sum: {ratios_sum}")


if __name__ == "__main__":
    main()
