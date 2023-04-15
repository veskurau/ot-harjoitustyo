class Question:
    """Class represents a single question in the game.

    Attributes:
        question: String, the question which is asked.
        answers: Dictionary, keys are the four answer options and the values
        has a boolean value which represents if the answer is correct or not
    """

    def __init__(self, question: str, category: str, answers: dict):
        self.question = question
        self.category = category
        self.answers = answers

    def __str__(self):
        return f"kysymys: {self.question}, vastausvaihtoehdot: {self.answers}"
