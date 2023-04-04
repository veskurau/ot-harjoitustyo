from entities.player import Player
from repositories.player_repository import PlayerRepository

class UI:
    """ The interface which interacts with the player
    """

    def __init__(self):
        self.pelaajat = PlayerRepository()

    def start(self):
            name = str(input("Mikä on nimesi? "))
            if self.pelaajat.find_player(name) is not None:
                print("Tervetuloa uudestaan pelaamaan", name)
            else: 
                print("Tervetuloa pelaamaan ensikertalainen!")
                self.pelaajat.create(name)   

    