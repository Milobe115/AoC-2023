def main():
    with open("./input.txt", "r") as f:
        lines = f.readlines()
    score_sum = 0

    for line in lines:
        hd, tl = line.split(":")
        numbers_scratched_str, winning_numbers_str = tl.split("|")
        numbers_scratched = [int(x) for x in numbers_scratched_str.split() if x != ""]
        winning_numbers = [int(x) for x in winning_numbers_str.split() if x != ""]
        winning_numbers_scratched = len(set(winning_numbers).intersection(set(numbers_scratched)))
        score_sum += pow(2, winning_numbers_scratched - 1) if winning_numbers_scratched > 0 else 0

    print(f"Score : {score_sum}")


if __name__ == "__main__":
    main()
