from card_handler import Card
from random import shuffle


class Deck:
    def __init__(self):
        self.cards = []
        for s in range(4):
            for v in range(2, 15):
                self.cards.append(Card(s, v))
        shuffle(self.cards)

    def remove_card(self):
        if len(self.cards) == 0:
            return "There are no more cards in the deck."
        return self.cards.pop()
