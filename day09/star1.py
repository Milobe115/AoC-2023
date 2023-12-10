import re


def main():
    with open("input.txt", 'r') as f:
        lines = f.read().splitlines()

    score = 0
    for line in lines:
        history = [[int(val) for val in line.split(" ")]]

        while set(history[-1]) != {0}:
            old_sequence = history[-1]
            new_sequence = []
            for i in range(len(old_sequence) - 1):
                new_sequence.append(old_sequence[i + 1] - old_sequence[i])
            history.append(new_sequence)

        for i in range(len(history) - 2, -1, -1):
            history[i].append(history[i][-1] + history[i + 1][-1])

        score += history[0][-1]

    print(f"Score: {score}")



if __name__ == "__main__":
    main()
