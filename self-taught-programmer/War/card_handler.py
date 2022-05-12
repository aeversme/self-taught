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
        self.name = self.values[self.value] + " of " + self.suits[self.suit]

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
        return self.name
