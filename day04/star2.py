class Card:
    winning_numbers_scratched: int
    number_of_cards: int

    def __init__(self, winning_numbers_scratched):
        self.winning_numbers_scratched = winning_numbers_scratched
        self.number_of_cards = 1


def main():
    with open("./input.txt", "r") as f:
        lines = f.readlines()
    score_sum = 0

    cards = []

    for line in lines:
        _, tl = line.split(":")
        numbers_scratched_str, winning_numbers_str = tl.split("|")
        numbers_scratched = [int(x) for x in numbers_scratched_str.split() if x != ""]
        winning_numbers = [int(x) for x in winning_numbers_str.split() if x != ""]
        winning_numbers_scratched = len(set(winning_numbers).intersection(set(numbers_scratched)))
        cards.append(Card(winning_numbers_scratched))

    for card_id in range(len(cards)):
        if cards[card_id].winning_numbers_scratched > 0:
            for i in range(1, cards[card_id].winning_numbers_scratched + 1):
                cards[card_id + i].number_of_cards += cards[card_id].number_of_cards

    print(f"Score : {sum([card.number_of_cards for card in cards])}")


if __name__ == "__main__":
    main()
