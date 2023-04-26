class Question:
    """Class, represents a single question in the game.

    Attributes:
        category (str): Category of the question (maantiede, viihde, historia ja yhteiskunta, 
                kirjallisuus ja taide, luonto ja tiede sekä urheilu ja vapaa-aika).
        question (str): The question which is asked.
        answers (list): Answer options
        correct_answer (int): Gives the index of the right answer in the answers-list
    """

    def __init__(self, category: str, question: str, answers: list, correct_answer: int):
        """Class constructor, which creates a new question.

        Args:
            category (str): The category of the question.
            question (str): The question itself.
            answers (list): 2-4 answer options, from which one is the correct one.
            correct_answer (int): Indicates which of the 2-4 answer options is the right one.
        """
        self.category = category
        self.question = question
        self.answers = answers
        self.correct_answer = correct_answer

    def __str__(self):
        text = ("kysymys:", self.question, "kategoria:", self.category, "vastausvaihtoehdot:",
                self.answers, "oikea vastaus:", self.correct_answer)
        return str(text)
