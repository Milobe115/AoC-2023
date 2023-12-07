import re
from math import sqrt, ceil, floor


def main():
    with open("test.txt", 'r') as f:
        lines = f.read().splitlines()

    times = [int(x) for x in re.findall(r"\d+", lines[0])]
    distances = [int(x) for x in re.findall(r"\d+", lines[1])]

    score = 1

    for i in range(len(times)):
        time = times[i]
        distance = distances[i]

        delta = sqrt(time ** 2 - 4 * distance)
        t0 = (time - delta) / 2
        t1 = (time + delta) / 2
        score *= max(ceil(t1) - floor(t0) - 1, 0)

    print(score)


if __name__ == "__main__":
    main()
