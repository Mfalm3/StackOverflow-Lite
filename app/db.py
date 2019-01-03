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
questions_db = [{
    'question_id': 1,
    'user_id': 1,
    'question': 'How do you install pip in Ubuntu?',
    'created_at': 'Fri 14 Dec 2018 01:41:59 AM ',
    'updated_at': '',
    'answers': [
            {
                "answer_id": 1,
                "question_id": 1,
                "answer_body": "Run sudo apt-get install python-pip",
                "user_id": 2,
                'created_at': 'Sat 15 Dec 2018 01:41:59 AM ',
            },
            {
                "answer_id": 2,
                "question_id": 1,
                "answer_body": "Have you tried sudo apt-get install python-pip",
                "user_id": 3,
                'created_at': 'Sat 15 Dec 2018 01:41:59 AM ',
            }
        ]
    },
    {
        'question_id': 2,
        'user_id': 1,
        'created_at': 'Sat 15 Dec 2018 01:41:59 AM ',
        'updated_at': '',
        'question': 'What does \'name not defined\' in my python code mean?',
        'answers': []
    }
]


def init_db():
    database = db
    return database


def init_test_db():
    database = test_db
    return database


def init_quiz_db():
    database = questions_db
    return database
