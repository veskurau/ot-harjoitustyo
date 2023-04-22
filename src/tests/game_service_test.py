import unittest
from services.game_service import GameService
from entities.player import Player


class TestGameService(unittest.TestCase):
    def setUp(self):
        self.game_service = GameService()

    def test_constructor_and_add_player_works(self):
        self.game_service.add_player("Pasi")
        self.assertEqual(str(self.game_service.player_scores), "{'Pasi': 0}")
