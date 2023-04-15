from entities.player import Player


class PlayerRepository:
    """ The class is responsible for the players database operations."""

    # Alustavasti tiedot tallennettu vain listaan/sanakirjaan

    def __init__(self):
        self.players = {}

    def create(self, name: str):
        if name not in self.players:
            self.players[name] = Player(name)
        else:
            print("Pelaaja on jo olemassa")

    def find_player(self, name: str):
        if name in self.players:
            return self.players[name]
        return None
