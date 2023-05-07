import subprocess
import sys
import time
from services.game_service import GameService


class UI:
    """ Class, the interface which interacts with the player.

    Attributes:
        game: GameService-object
        _winner: Tuple, contains (bool,str). Where boolean tells if winner is found and str the name
    """

    def __init__(self):
        """Class constructor, which creates a new interface."""

        self._game = GameService()
        self._winner = (False, None)

    def start(self):
        """Starts up the game-interface for the player."""

        self._beginning_view()
        self._choose_players()
        self._start_rounds()
        self._declare_winner_and_end_game()

    def _beginning_view(self):
        # The first view
        while True:
            print()
            print("Komennot: ")
            print("1: Aloita uusi peli")
            print("2: Lisää uusia kysymyksiä")
            print("x: Poistu pelistä")
            print()
            action = str(input("Komento: "))
            if action == "1":
                print("Tervetuloa pelaamaan!")
                return
            elif action == "2":
                print("Uusien kysymysten lisäys -toiminto tulee peliin myöhemmin.")
                print(
                    "Voit käydä lisäämässä kysymyksiä data-kansiossa sijaitsevaan csv-tiedostoon.")
            elif action == "x":
                sys.exit("Hyvästi!")
            else:
                print("Anna validi komento!")

    def _choose_players(self):
        # Choosing the player count and names
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
                while True:
                    name = str(input(f"Pelaajan {i} nimi: "))
                    if name == "":
                        print("Anna jokin nimi!")
                        print()
                        continue
                    self._game.add_player(name)
                    break
            self._clear_view()
            print("Kiitos. Pelaajat on lisätty.")
            print(
                "Ensimmäisenä kaikkiin kuuteen aihealueeseen vastannut pelaaja voittaa pelin!")
            return

    def _start_rounds(self):
        # Starting the actual game rounds
        while True:
            # Choosing a player and a question
            for name in self._game.player_scores:
                answer_streak = True
                while answer_streak is True:
                    question = self._game.get_question()
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
                    # Checking the player's answer
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
                        self._game.add_correctly_answered_category(
                            name, question.category)
                    else:
                        print(
                            f"Vastauksesi {action} oli valitettavasti väärin. "
                            f"Oikea vastaus olisi ollut {question.correct_answer}")
                        answer_streak = False
                    time.sleep(4)
                    self._clear_view()
                    # Check if a winner is found
                    self._winner = self._game.someone_has_full_score()
                    if self._winner[0]:
                        return
            print()
            print("Pelitilanne on seuraavanlainen:")
            self._game.print_scores()

    def _declare_winner_and_end_game(self):
        for i in [".", "..", "...", "...."]:
            print(i)
            time.sleep(1)

        print(
            f"ONNEKSI OLKOON {self._winner[1]}, OLET VOITTAJA!")
        time.sleep(3)
        print()
        print("Lopullinen pistetilanne:")
        self._game.print_scores()
        sys.exit()

    def _clear_view(self):
        """Clears the screen in text-interface"""

        subprocess.run("clear", check=True)

    def _print_existing_players(self):
        players = self._game.get_existing_players()
        for player in players:
            print(f"{player.name}: {player.wins} voittoa")
