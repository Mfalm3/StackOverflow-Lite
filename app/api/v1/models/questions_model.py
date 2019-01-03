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

    def answer(self, id, question_id, answer_body):
        """Post answers to question."""
        db = self.db
        answer_data = {
            "answer_id": len(db[question_id-1]['answers'])+1,
            "question_id": question_id,
            "answer_body": answer_body,
            "user_id": id,
            'created_at': datetime.datetime.now(),
        }
        return (db[question_id-1]['answers']).append(answer_data)

    def delete(self, question_id):
        """Delete a question method."""
        db = self.db
        del(db[question_id-1])
        return db
