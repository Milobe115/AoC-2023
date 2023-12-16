def parse_patterns(lines):
    patterns = []
    pattern = []
    for line in lines:
        if line == "":
            patterns.append(pattern)
            pattern = []
        else:
            pattern.append(line)
    patterns.append(pattern)
    return patterns


def find_pattern_score(pattern, allowed_errors=0):
    for col in range(len(pattern[0]) - 1):
        errors = 0
        for split_col in range(len(pattern[0])):
            left = col - split_col
            right = col + 1 + split_col
            if 0 <= left < right < len(pattern[0]):
                for row in range(len(pattern)):
                    if pattern[row][left] != pattern[row][right]:
                        errors += 1
        if errors == allowed_errors:
            return col + 1

    for row in range(len(pattern) - 1):
        errors = 0
        for split_row in range(len(pattern)):
            up = row - split_row
            down = row + 1 + split_row
            if 0 <= up < down < len(pattern):
                for col in range(len(pattern[0])):
                    if pattern[up][col] != pattern[down][col]:
                        errors += 1
        if errors == allowed_errors:
            return (row + 1) * 100


def main():
    with open("input.txt", 'r') as f:
        lines = f.read().splitlines()

    patterns = parse_patterns(lines)
    scores = [find_pattern_score(pattern, 1) for pattern in patterns]
    print(sum(scores))


if __name__ == "__main__":
    main()
