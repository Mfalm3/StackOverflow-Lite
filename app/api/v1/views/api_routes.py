from flask import Blueprint, jsonify, request

from app.api.v1.models.users_model import UserModel
from app.api.v1.models.questions_model import QuestionModel
from app.db import init_quiz_db
from app.api.v1.utils.utils import requires_token


v1 = Blueprint("v1", __name__, url_prefix="/api/v1/")
user = UserModel()
quiz = QuestionModel()


@v1.route('/signin', methods=['POST'])
def signin():
    """Auth endpoint."""
    data = request.json
    if not all([data.get("email"), data.get("password")]):
        return jsonify({
            "status": "error",
            "message": "Missing field(s) (email, password)"
        }), 400

    return user.auth(data.get("email"), data.get("password"))


@v1.route('/signup', methods=['POST'])
def signup():
    """Create user account endpoint."""
    data = request.json
    username = data['username']
    email = data['email']
    password = data['password']
    if not all([data.get("username"), data.get("email"), data.get("password")]):
        return jsonify({
            "status": "error",
            "message": "Missing field(s) (username, email, password)"
        }), 400

    return user.save(username, email, password)


@v1.route('/', methods=['GET'])
def questions():
    """View all questions endpoint."""

    return jsonify({
        "questions": quiz.view_questions()
    })


@v1.route('/question/<int:id>', methods=['GET'])
def view_answers(id):
    """View all answers to a question endpoint."""

    return jsonify({
        "question_details": quiz.view_answers(id)
    })


@requires_token
@v1.route('/questions', methods=['POST'])
def ask_question():
    """Ask a new question endpoint."""
    data = request.json
    if data == '' or data is None:
        return jsonify({
            "status": "error",
            "message": "Missing field/s (user_id, question_brief, question_description)"
        }), 409
    id = data.get('user_id')
    question_brief = data.get('question_brief')
    question_description = data.get('question_description')
    quiz.ask(id, question_brief, question_description)
    return jsonify({
        "status": "success",
        "message": "Question created successfully!"
    }), 201
