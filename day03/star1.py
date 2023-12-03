import re
from dataclasses import dataclass


@dataclass
class Number:
    line: int
    value: int
    start: int
    end: int
    is_valid: bool

    def __init__(self, line: int = 0, value: int = 0, start: int = 0, end: int = 0):
        self.line = line
        self.value = value
        self.start = start
        self.end = end
        self.is_valid = False


@dataclass
class Symbol:
    value: str
    line: int
    col: int

    def __init__(self, value: str = '', line: int = 0, col: int = 0):
        self.value = value
        self.line = line
        self.col = col


def extract_numbers(lines: list[str]) -> list[Number]:
    numbers = []
    for line in range(len(lines)):
        for match in re.finditer(r"(\d+)", lines[line]):
            number = Number(line, int(match.group()), match.start(), match.end()-1)
            numbers.append(number)
    return numbers


def extract_symbols(lines: list[str]) -> list[Symbol]:
    symbols = []
    for line in range(len(lines)):
        for match in re.finditer(r"([^\d.])", lines[line]):
            symbol = Symbol(match.group(), line, match.start())
            symbols.append(symbol)
    return symbols


def main():
    with open("./input.txt", "r") as f:
        lines = list(map(lambda x: x.strip(), f.readlines()))
    numbers = extract_numbers(lines)
    symbols = extract_symbols(lines)

    parts_sum = 0

    for number in numbers:
        for symbol in symbols:
            if number.line - 1 <= symbol.line <= number.line + 1 and number.start - 1 <= symbol.col <= number.end + 1:
                number.is_valid = True
                break

        if number.is_valid:
            parts_sum += number.value

    print(f"Sum: {parts_sum}")


if __name__ == "__main__":
    main()
