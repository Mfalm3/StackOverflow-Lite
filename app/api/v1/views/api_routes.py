from flask import Blueprint, jsonify, request
from app.api.v1.models.users_model import UserModel


v1 = Blueprint("v1", __name__, url_prefix="/api/v1/")
user = UserModel()


@v1.route('/signin')
def signin():
    """Auth endpoint."""
    pass


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
