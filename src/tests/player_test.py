import unittest
from entities.player import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("Harri")

    def test_constructor_sets_points_and_name_right(self):
        answer = str(self.player)
        self.assertEqual(answer, "nimi: Harri, pisteet: 0")
        