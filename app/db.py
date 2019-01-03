from flask_bcrypt import generate_password_hash

db = [{
    "username": "dev",
    "email": "newuser@company.com",
    "password": generate_password_hash("newuserpassword")
}]
test_db = [{
    "username": "test",
    "email": "newuser@company.com",
    "password": "newuserpassword"
}]


def init_db():
    database = db
    return database


def init_test_db():
    database = test_db
    return database
