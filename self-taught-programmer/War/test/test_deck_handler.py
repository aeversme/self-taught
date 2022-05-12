from ..deck_handler import Deck


def test_deck_size():
    deck = Deck()

    assert len(deck.cards) == 52


def test_deck_contents():
    deck = Deck()

    assert any(card.name == "Ace of spades" for card in deck.cards)
    assert any(card.name == "5 of diamonds" for card in deck.cards)


def test_remove_card():
    deck = Deck()
    removed_card = deck.remove_card()

    assert len(deck.cards) == 51
    assert removed_card.name not in deck.cards
