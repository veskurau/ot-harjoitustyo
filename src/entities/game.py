# Voi olla että tätä luokkaa ei tarvita, vaan annetaan GameService luokan hoitaa vastaavat tehtävät,
# mutta annetaan luokan olla vielä toistaikseksi olemassa

class Game:
    """ Class represents a single game which the selected 
        players will play.

    Attributes:
        player_scores: Dictionary, keeps track of the players in current game and their scores.
    """

    def __init__(self):
        self.player_scores = {}

    def __str__(self):
        return f"player_scores: {self.player_scores}"
