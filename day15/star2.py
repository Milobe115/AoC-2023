import re
from dataclasses import dataclass
from functools import cache


@cache
def calc_hash(string):
    hash = 0
    for char in string:
        hash += ord(char)
        hash = (hash * 17) % 256
    return hash


@dataclass
class Operation:
    code: str
    focal: int


def main():
    with open("input.txt", 'r') as f:
        line = f.read().splitlines()[0]

    instructions = re.findall(r"[^,]+", line)
    boxes: dict[int, list[Operation]] = {}

    for instruction in instructions:
        if "=" in instruction:
            code = re.search(r"\w+", instruction).group()
            focal = int(re.search(r"\d+", instruction).group())
            hash = calc_hash(code)
            if hash in boxes:
                if any(map(lambda x: x.code == code, boxes[hash])):
                    for op in boxes[hash]:
                        if op.code == code:
                            op.focal = focal
                else:
                    boxes[hash].append(Operation(code, focal))
            else:
                boxes[hash] = [Operation(code, focal)]

        elif "-" in instruction:
            code = re.search(r"\w+", instruction).group()
            hash = calc_hash(code)
            if hash in boxes:
                boxes[hash] = [op for op in boxes[hash] if op.code != code]

    score = 0
    for key, box in boxes.items():
        for idx, op in enumerate(box):
            score += (key + 1) * (idx + 1) * op.focal
    print(score)


if __name__ == "__main__":
    main()
