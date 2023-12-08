import re


def parse_map(lines):
    node_map = {}
    for line in lines:
        node, left, right = re.findall(r"\w{3}", line)
        node_map[node] = (left, right)
    return node_map


def main():
    with open("input.txt", 'r') as f:
        lines = f.read().splitlines()

    instructions = lines[0]
    node_map = parse_map(lines[2:])

    curr_node = 'AAA'
    score = 0
    while curr_node != "ZZZ":
        curr_node = node_map[curr_node][0] if instructions[score % len(instructions)] == "L" else node_map[curr_node][1]
        score += 1

    print(score)


if __name__ == "__main__":
    main()
