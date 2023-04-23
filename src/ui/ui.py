# from entities.player import Player <- saatetaan tarvita myöhemmin
from repositories.player_repository import PlayerRepository
from services.game_service import GameService


class UI:
    """ The interface which interacts with the player."""

    def __init__(self):
        self.game = GameService()

    def start(self):
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
            for i in range(1, count+1):
                name = str(input(f"Pelaajan {i} nimi: "))
                self.game.add_player(name)
            print("Kiitos. Pelaajat on lisätty.")
            print(
                "Ensimmäisenä kaikkiin kahdeksaan aihealueeseen vastannut pelaaja voittaa pelin!")
            break

        # Starting the actual rounds
        while True:
            # Choosing a player and a question
            for name, score in self.game.player_scores.items():
                answer_streak = True
                while answer_streak is True:
                    question = self.game.get_question()
                    print()
                    print()
                    print("Seuraavana vuorossa on", name)

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
                    if question.correct_answer == action:
                        print(f"Vastaus {action} oli oikein!")
                        self.game.add_correctly_answered_category(name, question.category)
                    else:
                        print(
                            f"Vastauksesi {action} oli valitettavasti väärin. Oikea vastaus olisi ollut {question.correct_answer}")
                        answer_streak = False
                
            print()
            print("Pelitilanne on seuraavanlainen:")
            self.game.print_scores()
            if self.game.someone_has_full_score()[0]:
                print(
                    f"ONNEKSI OLKOON {self.game.someone_has_full_score()[1]}, OLET VOITTAJA!")
                break
