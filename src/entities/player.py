class Player:
    """ Class represents a single player in the game.

    Attributes:
        name (str): Name of the player.
        wins (int): How many games has the player won.
    """

    def __init__(self, name: str, wins: int):
        """Class constructor, which creates a new player.

        Args:
            name (str): Name of the player.
            wins (int): Number of games won.
        """
        self.name = name
        self.wins = wins

    def __str__(self):
        return f"nimi: {self.name}, voitot: {self.wins}"
