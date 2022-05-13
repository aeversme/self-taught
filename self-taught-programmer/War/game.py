from deck_handler import Deck
from player_handler import Player


class Game:
    def __init__(self):
        name1 = input("Player 1 name: ")
        name2 = input("Player 2 name: ")
        self.deck = Deck()
        self.player1 = Player(name1)
        self.player2 = Player(name2)

    def winner(self, player1, player2):
        if player1.wins > player2.wins:
            return player1.name, player1.wins
        if player2.wins > player1.wins:
            return player2.name, player2.wins
        return "It was a tie!", None

    def play_game(self):
        cards = self.deck.cards
        print("Let's play War!")
        while len(cards) >= 2:
            response = input("Enter 'q' to quit, any other key to play: ")
            if response == 'q':
                break
            p1card = self.deck.remove_card()
            p2card = self.deck.remove_card()
            print("  {} drew the {}, and {} drew the {}".format(self.player1.name,
                                                                p1card.name,
                                                                self.player2.name,
                                                                p2card.name))
            if p1card > p2card:
                round_winner = self.player1
            else:
                round_winner = self.player2
            round_winner.wins += 1
            print("    {} wins this round!".format(round_winner.name))
        print("This game of War is over.")
        game_winner, wins = self.winner(self.player1, self.player2)
        if game_winner == "  It was a tie!":
            print(game_winner)
        else:
            print("  {} won the game by winning {} of 26 rounds. Congratulations!".format(game_winner, wins))


game = Game()
game.play_game()
