from collections import Counter
from enum import IntEnum
from functools import cmp_to_key


class HandType(IntEnum):
    HIGH_CARD = 1
    PAIR = 2
    TWO_PAIR = 3
    THREE = 4
    FULL_HOUSE = 5
    FOUR = 6
    FIVE = 7


class Hand:
    cards: list[str]
    bet: int

    def __init__(self, cards, bet):
        self.cards = cards
        self.bet = bet

    def hand_type(self):
        possible_cards = "23456789TQKA"
        final_type = HandType.HIGH_CARD
        for new_card in possible_cards:
            modified_hand = map(lambda x: x.replace("J", new_card), self.cards)
            counter = Counter(modified_hand)
            match len(counter):
                case 1:
                    final_type = max(final_type, HandType.FIVE)
                case 2:
                    final_type = max(final_type, HandType.FOUR) if set(counter.values()) == {4, 1} else max(final_type,
                                                                                                            HandType.FULL_HOUSE)
                case 3:
                    final_type = max(final_type, HandType.THREE) if set(counter.values()) == {3, 1} else max(final_type,
                                                                                                             HandType.TWO_PAIR)
                case 4:
                    final_type = max(final_type, HandType.PAIR)
                case 5:
                    final_type = max(final_type, HandType.HIGH_CARD)
        return final_type


def compare_cards(card_1, card_2):
    card_ranks = "J23456789TQKA"
    return card_ranks.find(card_1) - card_ranks.find(card_2)


def compare_hands(hand_1, hand_2):
    i = 0
    while i < len(hand_1.cards) and compare_cards(hand_1.cards[i], hand_2.cards[i]) == 0:
        i += 1

    return compare_cards(hand_1.cards[i], hand_2.cards[i])


def main():
    with open("input.txt", 'r') as f:
        lines = f.read().splitlines()

    score = 0

    hands = [Hand(list(hand.split(" ")[0]), int(hand.split(" ")[1])) for hand in lines]
    separated_hands = [[hand for hand in hands if hand.hand_type() == value] for value in HandType]

    for hand_type in separated_hands:
        hand_type.sort(key=cmp_to_key(compare_hands))

    sorted_hands = [item for sub_list in separated_hands for item in sub_list]

    for i, hand in enumerate(sorted_hands):
        score += (i + 1) * hand.bet
    print(score)


if __name__ == "__main__":
    main()
