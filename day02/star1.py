import re


def main():
    with open("./input.txt", "r") as f:
        lines = list(map(lambda x: x.strip(), f.readlines()))

    id_sums = 0

    for line in lines:
        hd, tl = line.split(": ")
        id = int(re.findall(r"\d+", hd)[0])
        game_bag = {"red": 0, "blue": 0, "green": 0}
        games = tl.split("; ")

        for game in games:
            tmp_bag = {"red": 0, "blue": 0, "green": 0}
            blocks = game.split(", ")
            for block in blocks:
                tmp = block.split(" ")
                color = tmp[1]
                tmp_bag[color] += int(tmp[0])
            game_bag["red"] = max(tmp_bag["red"], game_bag["red"])
            game_bag["blue"] = max(tmp_bag["blue"], game_bag["blue"])
            game_bag["green"] = max(tmp_bag["green"], game_bag["green"])

        if game_bag["red"] <= 12 and game_bag["blue"] <= 14 and game_bag["green"] <= 13:
            id_sums += id

    print(f"Final id sum = {id_sums}")


if __name__ == "__main__":
    main()
