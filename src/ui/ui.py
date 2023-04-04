from entities.player import Player
from repositories.player_repository import PlayerRepository

class UI:
    """ The interface which interacts with the player
    """

    def __init__(self):
        self.pelaajat = PlayerRepository()

    def start(self):
        while True:
            name = str(input("Mikä on nimesi? "))
            print("self.pelaajat.find_player(name) =", self.pelaajat.find_player(name))
            if self.pelaajat.find_player(name) is not None:
                print("Tervetuloa uudestaan pelaamaan", name)
            else: 
                print("Tervetuloa pelaamaan ensikertalainen!")
                self.pelaajat.create(name)   

    