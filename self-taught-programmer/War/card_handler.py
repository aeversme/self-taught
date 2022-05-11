class Card:
    suits = ("clubs", "diamonds", "hearts", "spades")
    values = (None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace")

    def __init__(self, s, v):
        """
        :param s: int <= 3
        :param v: int <= 14
        """
        self.suit = s
        self.value = v

    def __lt__(self, other):
        if self.value < other.value:
            return True
        if self.value == other.value:
            if self.suit < other.suit:
                return True
            return False
        return False

    def __gt__(self, other):
        if self.value > other.value:
            return True
        if self.value == other.value:
            if self.suit > other.suit:
                return True
            return False
        return False

    def __repr__(self):
        return self.values[self.value] + " of " + self.suits[self.suit]


card1 = Card(2, 10)
card2 = Card(3, 10)
card3 = Card(0, 13)
print(card1 > card2)
print(card3 > card2)
