# from entities.player import Player <- saatetaan tarvita myöhemmin
from repositories.player_repository import PlayerRepository
from services.game_service import GameService


class UI:
    """ The interface which interacts with the player."""
    

    def __init__(self):
        self.game = GameService()

    def start(self):
        while True:
            print()
            print("Komennot: ")
            print("1: Aloita uusi peli")
            print("2: Lisää uusia kysymyksiä")
            print()
            action = str(input("Komento: "))
            if action == "1":
                print("Tervetuloa pelaamaan!")
                break
            elif action == "2":
                print("Uusien kysymysten lisäys -toiminto tulee myöhemmin")
            else:
                print("Anna validi komento!")

        while True:
            print()
            count = int(input("Montako pelaajaa pelaa (1-5 pelaajaa): "))
            if count not in [1,2,3,4,5]:
                print("Anna validi pelaajamäärä (1-5 pelaajaa)!")
                continue
            for i in range(1,count+1):
                name = str(input(f"Pelaajan {i} nimi: "))
                self.game.add_player(name)
            print("Kiitos. Pelaajat on lisätty ja peli voi alkaa!")
            break

        print("pelaajat:", self.game)
        print("Peli alkaa tästä....")
