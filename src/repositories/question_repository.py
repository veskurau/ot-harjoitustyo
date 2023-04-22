from entities.question import Question
from config import QUESTIONS_FILE_PATH


class QuestionRepository:
    """The class is responsible for the questions-database operations."""

    def __init__(self, file_path):
        """The constructor.

        Args:
            file_path: The path to the csv-file with all the questions
        """

        self._file_path = file_path

    def get_all(self):
        """Returns all the questions.

        Returns:
            Returns a list of Question-objects.
        """
        return self._read()

    def create(self):
        pass

    def _read(self):
        questions = []

        with open(self._file_path, encoding="utf-8") as file:
            for row in file:
                row = row.replace("\n", "")
                parts = row.split(";")

                category = parts[0]
                question = parts[1]
                answers = []
                answers = parts[2:-1]
                correct_answer = int(parts[-1])

                questions.append(
                    Question(category, question, answers, correct_answer))
        return questions


question_repository = QuestionRepository(QUESTIONS_FILE_PATH)
