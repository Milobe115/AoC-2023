import re


def calc_hash(string):
    hash = 0
    for char in string:
        hash += ord(char)
        hash = (hash * 17) % 256
    return hash


def main():
    with open("input.txt", 'r') as f:
        line = f.read().splitlines()[0]

    instructions = re.findall(r"[^,]+", line)
    hashes = map(calc_hash, instructions)
    print(sum(hashes))


if __name__ == "__main__":
    main()
