import subprocess
import time
from services.game_service import GameService


class UI:
    """ Class, the interface which interacts with the player.

    Attributes:
        game: GameService-object
    """

    def __init__(self):
        """Class constructor, which creates a new interface."""

        self.game = GameService()

    def start(self):
        """Starts up the game-interface for the player."""

        # The first view
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

        # Choosing the player count
        while True:
            print()
            try:
                count = int(input("Montako pelaajaa pelaa (1-5 pelaajaa): "))
            except ValueError:
                print("Anna vastaus numerona!")
                continue
            if count not in [1, 2, 3, 4, 5]:
                print("Anna validi pelaajamäärä (1-5 pelaajaa)!")
                continue
            print()
            print("Aiemmat pelaajat: ")
            self._print_existing_players()
            print()

            for i in range(1, count+1):
                name = str(input(f"Pelaajan {i} nimi: "))
                self.game.add_player(name)
            self._clear_view()
            print("Kiitos. Pelaajat on lisätty.")
            print(
                "Ensimmäisenä kaikkiin kahdeksaan aihealueeseen vastannut pelaaja voittaa pelin!")
            break

        # Starting the actual rounds
        while True:
            # Choosing a player and a question
            for name in self.game.player_scores:
                answer_streak = True
                while answer_streak is True:
                    question = self.game.get_question()
                    print()
                    print()
                    print("Vuorossa on", name)
                    print("Kategoriasi on:", question.category)
                    print()
                    print("Kysymyksesi on:")
                    print(question.question)
                    print()
                    print("Vastausvaihtoehtosi ovat:")
                    i = 1
                    for answer in question.answers:
                        print(f"{i}) {answer}")
                        i += 1
                    # Checking the players answer
                    while True:
                        print()
                        try:
                            action = int(input("Anna vastauksesi: "))
                        except ValueError:
                            print("Anna vastaus numerona!")
                            continue
                        if action <= 0 or action > len(question.answers):
                            print("Anna oikea numero!")
                            continue
                        break
                    print()
                    time.sleep(3)
                    if question.correct_answer == action:
                        print(f"Vastaus {action} oli oikein!")
                        self.game.add_correctly_answered_category(
                            name, question.category)
                    else:
                        print(
                            f"Vastauksesi {action} oli valitettavasti väärin. "
                            f"Oikea vastaus olisi ollut {question.correct_answer}")
                        answer_streak = False
                    time.sleep(4)
                    self._clear_view()
            print()
            print("Pelitilanne on seuraavanlainen:")
            self.game.print_scores()
            if self.game.someone_has_full_score()[0]:
                print(
                    f"ONNEKSI OLKOON {self.game.someone_has_full_score()[1]}, OLET VOITTAJA!")
                break

    def _clear_view(self):
        """Clears the screen in text-interface"""

        subprocess.run("clear", check=True)

    def _print_existing_players(self):
        players = self.game.get_existing_players()
        for player in players:
            print(f"{player.name}: {player.wins} voittoa")
