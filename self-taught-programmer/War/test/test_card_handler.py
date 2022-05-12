from ..card_handler import Card


def test_cards():
    card1 = Card(1, 5)
    card2 = Card(2, 9)
    card3 = Card(3, 9)
    card4 = Card(0, 12)

    assert card1 < card2
    assert card3 > card2
    assert card3 < card4
