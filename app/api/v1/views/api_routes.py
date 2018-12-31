from flask import Blueprint, jsonify, request, make_response
from flask_bcrypt import Bcrypt
from app.api.v1.utils.validator import Validator

import jwt
import datetime

v1 = Blueprint("v1", __name__, url_prefix="/api/v1/")

validate = Validator()
bcrypt = Bcrypt()

@v1.route("/")
def index():
    return jsonify('Hello World'), 201


@v1.route('/signin')
def signin():
    pass


@v1.route('/signup',methods=['POST'])
def signup():
    pass