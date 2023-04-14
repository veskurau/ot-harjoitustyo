class Player:
    """ Class represents a single player in the game
    """

    def __init__(self, name):
        self.name = name
        self.points = 0

    def __str__(self):
        return f"nimi: {self.name}, pisteet: {self.points}"
