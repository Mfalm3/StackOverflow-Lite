"""Questions model."""
from app.db import init_quiz_db


class QuestionModel:
    """Question Model class."""

    def __init__(self):
        """Initialize question model."""
        self.db = init_quiz_db()

    def view_questions(self):
        """View all quesitons."""
        questions = self.db
        return questions

    def view_answers(self, id):
        """View all answers to a question."""
        answers = self.db
        quiz_and_answers = answers[id-1]
        return quiz_and_answers
