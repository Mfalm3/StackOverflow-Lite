"""User Model."""
from flask import jsonify
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_jwt import jwt
import datetime

from app.api.v1.models.base_model import BaseModel
from app.api.v1.utils.validator import valid_email, email_exist,\
 username_exists
from app.db import init_db
from instance.config import key


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

    def get_user(self, email):
        current_user = [user for user in self.db if user['email'] == email]
        if current_user:
            return current_user[0]
        else:
            return False

    def auth(self, email, password):
        """Authenticate the user."""
        if valid_email(email):
            if email_exist(email, self.db):
                user = self.get_user(email)
                name = user['username']
                if username_exists(name, self.db):
                    if user and check_password_hash(user['password'], password):
                        data = {
                            "username": name,
                            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
                        }
                        token = jwt.encode(data, key, algorithm='HS256')

                        if token:
                            return jsonify({
                                "status": "success",
                                "message": "User signed in successfully!",
                                "token": token.decode('utf-8')
                            }), 201

                        else:
                            return make_response(jsonify({
                                "status": "error",
                                "message": "Password is incorrect. Please try again."
                            }), 400)
                    else:
                        return jsonify({
                            "message": "could not find user/password not incorrect"
                        }), 401
                else:
                    return jsonify({
                        "status": "error",
                        "message": "No user found with the given credentials"
                    }), 409
            else:
                return jsonify({
                    "status": "error",
                    "message": "No user found with the given credentials"
                }), 409
        else:
            return jsonify({
                "status": "error",
                "message": "Ensure your email is in the right format! eg. test@example.com"
            }), 409
