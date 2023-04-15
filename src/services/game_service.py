# from entities.game import Game <- Ei luultavasti tarvita
from entities.player import Player

# Todennäköisesti joudutaan importaamaan myös repositoriot

class GameService:
    """The class responsible for the application logic and represents a single game which the selected 
        players will play.

    Attributes:
        player_scores: Dictionary, keeps track of the players in current game and their scores.
    """

    def __init__(self):
    # Täytyy varmaan lisätä attribuutteja, kuten repositoriot ainakin
        self.player_scores = {}

    def add_player(self, name: str):
        new_player = Player(name)
        if new_player.name not in self.player_scores:
            self.player_scores[new_player.name] = new_player.points

    def get_player_score(self, name: str) -> str:
        return self.player_scores[name]

    def throw_dice(self):
        pass

    def __str__(self):
        return f"player_scores: {self.player_scores}"
