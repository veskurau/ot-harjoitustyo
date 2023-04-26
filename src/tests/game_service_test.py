import unittest
from services.game_service import GameService
from entities.question import Question
from tests.conftest import pytest_configure
# from entities.player import Player <- ei välttämättä tarvita


class TestGameService(unittest.TestCase):

    def setUp(self):
        self.game_service = GameService()
        pytest_configure()

    def situation_where_only_one_question(self):
        # Let's add only one question to the questions-list:
        # Maantiede;Mikä on Australian pääkaupunki?;Melbourne;Canberra;Sydney;Brisbane;2
        category = "Maantiede"
        question = "Mikä on Australian pääkaupunki?"
        answers = ["Melbourne", "Canberra", "Sydney", "Brisbane"]
        correct_answer = 2
        self.game_service.questions = [
            Question(category, question, answers, correct_answer)]

    def test_constructor_and_add_player_works(self):
        self.game_service.add_player("Pasi")
        self.assertEqual(str(self.game_service.player_scores), "{'Pasi': []}")
        # Adding the player with the same name again
        self.game_service.add_player("Pasi")
        self.assertEqual(str(self.game_service.player_scores), "{'Pasi': []}")

    def test_get_question_and_question_object(self):
        self.situation_where_only_one_question()
        return_value = self.game_service.get_question()
        self.assertEqual(str(return_value),
                         str(Question("Maantiede", "Mikä on Australian pääkaupunki?",
                                      ["Melbourne", "Canberra", "Sydney", "Brisbane"], 2)))

    def test_get_existing_players(self):
        self.game_service.add_player("Pasi")
        self.game_service.add_player("Kerttu")
        players = self.game_service.get_existing_players()
        self.assertEqual(str(players[0]), "nimi: Pasi, voitot: 0")
        self.assertEqual(str(players[1]), "nimi: Kerttu, voitot: 0")

    def test_adding_correct_answers_and_printing_scores(self):
        self.game_service.add_player("Pasi")
        self.game_service.add_correctly_answered_category("Pasi", "Maantiede")
        self.assertEqual(self.game_service.print_scores(),
                         print("\nPelaajalla Pasi on 1/8 pistettä \n"
                               "ja hän on vastannut oikein aiheisiin: ['Maantiede']"))
        self.game_service.add_correctly_answered_category(
            "Pasi", "Maantiede")  # When trying to add same category
        self.assertEqual(self.game_service.print_scores(),
                         print("\nPelaajalla Pasi on 1/8 pistettä \n"
                               "ja hän on vastannut oikein aiheisiin: ['Maantiede']"))

    def test_someone_has_full_score(self):
        self.game_service.add_player("Pasi")
        self.game_service.add_correctly_answered_category("Pasi", "Maantiede")
        self.assertEqual(
            self.game_service.someone_has_full_score(), (False, None))
        # Let's add 7 more strings to the list, so the score should be 8/8
        for i in range(7):
            self.game_service.add_correctly_answered_category("Pasi", str(i))
        self.assertEqual(
            self.game_service.someone_has_full_score(), (True, "Pasi"))
