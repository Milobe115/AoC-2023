def transpose(matrix):
    return tuple(map(lambda x: "".join(x), [*zip(*matrix)]))


def tilt(matrix, direction):
    trans = direction in "NS"
    reverse = direction in "NW"
    if trans:
        matrix = transpose(matrix)
    res = ()
    for row in matrix:
        res += ("#".join("".join(sorted(chunk, reverse=reverse)) for chunk in row.split("#")),)
    if trans:
        res = transpose(res)
    return res


def speen_cycle(matrix):
    for dir in "NWSE":
        matrix = tilt(matrix, dir)
    return matrix


def speen(matrix, N):
    result = matrix
    cache = {result: 0}
    i = 1
    while i <= N:
        result = speen_cycle(result)
        if result not in cache:
            cache[result] = i
        else:
            period = i - cache[result]
            idx = cache[result] + (N - cache[result]) % period
            for key, val in cache.items():
                if val == idx:
                    return key
        i += 1
    return result


def calc_score(matrix):
    height = len(matrix)
    score = 0
    for i, row in enumerate(matrix):
        score += (height - i) * row.count("O")
    return score


def main():
    with open("input.txt", 'r') as f:
        matrix = f.read().splitlines()

    matrix = tilt(matrix, 'N')
    matrix = speen(matrix, 1000000000)
    score = calc_score(matrix)
    print(score)


if __name__ == "__main__":
    main()