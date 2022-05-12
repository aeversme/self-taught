from ..player_handler import Player


def test_player_attributes():
    player = Player("George")

    assert player.wins == 0
    assert player.name == "George"
    assert player.card is None
