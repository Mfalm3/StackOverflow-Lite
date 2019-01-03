"""User Model."""
from flask import jsonify
from flask_bcrypt import generate_password_hash

from app.api.v1.models.base_model import BaseModel
from app.api.v1.utils.validator import valid_email, email_exist,\
 username_exists
from app.db import init_db


class UserModel(BaseModel):
    """Users Model Class."""

    def save(self, username, email, password):
        """Signup method."""
        self.db = init_db()
        new_user = {
            "username": username,
            "email": email,
            "password": generate_password_hash(password),
        }

        if valid_email(email):
            if email_exist(email, self.db):
                return jsonify({
                    "status": "error",
                    "message": "Email already exists! Perhaps you want to login?"
                }), 409
            else:
                if username_exists(username, self.db):
                    return jsonify({
                        "status": "error",
                        "message": "Username already exists. Please choose another username"
                    }), 409
                else:
                    self.db.append(new_user)
                    return jsonify({
                        "status": "success",
                        "message": "User created successfully!"
                    }), 201
        else:
            return jsonify({
                "status": "error",
                "message": "Ensure your email is in the right format! eg. test@example.com"
            }), 409
