from entities.game import Game
from entities.player import Player

# Todennäköisesti joudutaan importaamaan myös repositoriot

class GameService:
    """The class responsible for the application logic."""

    def __init__(self, game: Game):
    # Täytyy varmaan lisätä attribuutteja, kuten repositoriot ainakin
        self.game = game

    def add_player(self, player: Player):
        pass

    def throw_dice(self):
        pass
    