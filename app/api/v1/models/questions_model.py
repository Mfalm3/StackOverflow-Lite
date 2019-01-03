"""Questions model."""
import datetime
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

    def ask(self, id, question_brief, question_description):
        """Post a question method."""
        db = self.db
        question_data = {
            'question_id': len(db)+1,
            'user_id': id,
            'created_at': datetime.datetime.now(),
            'updated_at': '',
            'question_brief': question_brief,
            'question_description': question_description,
            'answers': []
        }
        return db.append(question_data)
