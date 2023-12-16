def transpose(matrix):
    return tuple(map(lambda x: "".join(x), [*zip(*matrix)]))


def tilt(matrix):
    matrix = transpose(matrix)
    res = ()
    for row in matrix:
        res += ("#".join("".join(sorted(chunk, reverse=True)) for chunk in row.split("#")),)
    res = transpose(res)
    return res


def calc_score(matrix):
    height = len(matrix)
    score = 0
    for i, row in enumerate(matrix):
        score += (height - i) * row.count("O")
    return score


def main():
    with open("input.txt", 'r') as f:
        matrix = f.read().splitlines()

    matrix = tilt(matrix)
    score = calc_score(matrix)
    print(score)


if __name__ == "__main__":
    main()
