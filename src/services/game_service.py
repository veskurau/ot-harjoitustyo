import random
from collections import defaultdict
# from entities.game import Game <- Ei luultavasti tarvita
from entities.player import Player

from repositories.question_repository import (
    question_repository as default_question_repository
)

# Todennäköisesti joudutaan importaamaan myös repositoriot
full_points = 8


class GameService:
    """The class responsible for the application logic and represents a single game 
        which the selected players will play.

    Attributes:
        player_scores: Dictionary, keeps track of the players in current game and their scores.
    """

    def __init__(self, question_repository=default_question_repository):
        # Täytyy varmaan lisätä attribuutteja, kuten repositoriot ainakin
        self.player_scores = defaultdict(list)
        self.question_repository = question_repository
        self.questions = self.question_repository.get_all()

    def add_player(self, name: str):
        new_player = Player(name)
        if new_player.name not in self.player_scores:
            self.player_scores[new_player.name] = []

    def get_player_scores(self):
        return self.player_scores

    def get_question(self):
        return self.questions.pop(random.randrange(len(self.questions)))

    def print_scores(self):
        for name, score in self.player_scores.items():
            print()
            print(f"Pelaajalla {name} on {len(score)}/{full_points} pistettä")
            print(f"ja hän on vastannut oikein aiheisiin: {score}")

    def someone_has_full_score(self):
        for name, score in self.player_scores.items():
            if len(score) == full_points:
                return (True, name)
        return (False, None)

    def throw_dice(self):
        pass

    def __str__(self):
        return f"player_scores: {self.player_scores}"
