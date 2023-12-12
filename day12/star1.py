from dataclasses import dataclass
from functools import cache


@cache
def count_arrangements(row: str, groups: tuple[int, ...]) -> int:
    hd = groups[0]
    tl_length = sum(groups[1:]) + len(groups) - 1
    count = 0
    for first_position in range(len(row) - tl_length - hd + 1):
        first_spring = '.' * first_position + '#' * hd + '.'
        if is_possible(first_spring, row):
            if len(groups) == 1:
                if all(char != '#' for char in row[len(first_spring):]):
                    count += 1
            else:
                count += count_arrangements(row[len(first_spring):], groups[1:])
    return count


def is_possible(spring: str, row: str) -> bool:
    if len(spring) > len(row):
        if any(char == '#' for char in spring[len(row):]):
            return False
    return all(char1 == char2 or char2 == '?' for char1, char2 in zip(spring, row))


def main():
    with open("input.txt", 'r') as f:
        lines = f.read().splitlines()

    input_data = []
    for line in lines:
        pattern, groups_str = line.split(" ")
        groups = tuple([int(x) for x in groups_str.split(",")])
        input_data.append((pattern, groups))

    score = 0

    for pattern, groups in input_data:
        local_score = count_arrangements(pattern, groups)
        score += local_score

    print(score)


if __name__ == "__main__":
    main()
