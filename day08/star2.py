import re
from math import lcm


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

    curr_nodes = [node for node in node_map.keys() if node[2] == 'A']
    dst_nodes = [node for node in node_map.keys() if node[2] == 'Z']
    node_score = [-1] * len(curr_nodes)
    score = 0
    while set(curr_nodes) != set(dst_nodes) and -1 in set(node_score):
        for idx, node in enumerate(curr_nodes):
            curr_nodes[idx] = node_map[node][0] if instructions[score % len(instructions)] == "L" else node_map[node][1]
            if curr_nodes[idx][2] == 'Z' and node_score[idx] == -1:
                node_score[idx] = score + 1
        score += 1

    f_score = 1
    for score in node_score:
        f_score = lcm(f_score, score)

    print(f_score)


if __name__ == "__main__":
    main()