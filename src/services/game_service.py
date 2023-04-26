import random
from entities.player import Player

from repositories.question_repository import (
    question_repository as default_question_repository
)

from repositories.player_repository import (
    player_repository as default_player_repository
)

# Todennäköisesti joudutaan importaamaan myös repositoriot
FULL_POINTS = 8


class GameService:
    """Class, responsible for the application logic and represents a single game 
        which the selected players will play.

    Attributes:
        player_scores: Dictionary, keeps track of the players in current game 
                       and which categories they have answered correctly.
                       Key is player name and value a list of correctly answered categories.
        question_repository: QuestionRepository-object, link to QuestionRepository-class
        questions: List, all the question from the repository
        player_repository: PlayerRepository-object, link to QuestionRepository-class
        players: List, all the players from the repository
    """

    def __init__(self, question_repository=default_question_repository,
                player_repository=default_player_repository):
        """Class constructor, which creates a new game.

        Args:
            question_repository: QuestionRepository-object, defaults to default_question_repository.
            player_repository: PlayerRepository-object, defaults to default_player_repository.
        """

        self.player_scores = {}
        self.question_repository = question_repository
        self.questions = self.question_repository.get_all()

        self.player_repository = player_repository
        self.players = self.player_repository.get_all()

    def add_player(self, name: str):
        """Adds a new player, if the player does not exist.

            Completely new player is also added to the SQLite-database. 

        Args:
            name (str): Name of the player.
        """
        # Adding the player to the player_scores dictionary, which tracks this current game
        new_player = Player(name, 0)
        if new_player.name not in self.player_scores:
            self.player_scores[new_player.name] = []

        # If player is not in the database, let's add it straight to the database
        if new_player.name not in [player.name for player in self.players]:
            self.player_repository.create(new_player.name)

    def add_correctly_answered_category(self, player_name: str, category: str):
        """When player answeres a question correctly, 
            the category in question is added to the player_scores attribute.

        Args:
            player_name (str): Name of the player.
            category (str): Category of the question.
        """

        if category not in self.player_scores[player_name]:
            self.player_scores[player_name].append(category)

    def get_existing_players(self):
        return self.players

    def get_player_scores(self):
        return self.player_scores

    def get_question(self) -> "Question":
        """Gets a random question from the questions-list.

        If the questions-list is empty, all the questions will be reloaded to the list.

        Returns:
            Question: Object which has the information of the question. 
        """

        if len(self.questions) == 0:
            self.questions = self.question_repository.get_all()
        return self.questions.pop(random.randrange(len(self.questions)))

    def print_scores(self):
        """Prints out the score of each player."""

        for name, score in self.player_scores.items():
            print()
            print(f"Pelaajalla {name} on {len(score)}/{FULL_POINTS} pistettä")
            print(f"ja hän on vastannut oikein aiheisiin: {score}")




    def someone_has_full_score(self) -> tuple:
        """Checks if some has answered correctly for all the categories. 

            Also adds +1 win for the winner in the SQLite-database.

        Returns:
            Tuple: (True, name) if someone has answered all categories correctly, else (False, None)
        """

        for name, score in self.player_scores.items():
            if len(score) == FULL_POINTS:
                self.player_repository.add_win(name)
                return (True, name)
        return (False, None)

    def __str__(self):
        return f"player_scores: {self.player_scores}"
