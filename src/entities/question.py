class Question:
    """Class represents a single question in the game.

    Attributes:
        category: String, category of the question (maantiede, viihde, historia ja yhteiskunta, 
                kirjallisuus ja taide, luonto ja tiede sekä urheilu ja vapaa-aika).
        question: String, the question which is asked.
        answers: List, answer options
        correct_answer: Integer, gives the index of the right answer in the answers-list
    """

    def __init__(self, category: str, question: str, answers: list, correct_answer: int):
        self.category = category
        self.question = question
        self.answers = answers
        self.correct_answer = correct_answer

    def __str__(self):
        text = ("kysymys:", self.question, "kategoria:", self.category, "vastausvaihtoehdot:",
                self.answers, "oikea vastaus:", self.correct_answer)
        return str(text)
