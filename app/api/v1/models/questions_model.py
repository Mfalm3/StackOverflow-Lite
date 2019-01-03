"""Questions model."""
from app.db import init_quiz_db


class QuestionModel:
    """Question Model class."""

    def view_questions(self):
        """View all quesitons."""
        self.db = init_quiz_db()
        return self.db
