import unittest
from app import create_app

class BaseTest(unittest.TestCase):
    """Test Environment setUp"""
    def setUp(self):
        self.client = create_app('testing')
        self.mime_type = 'application/json'
        self.login_url = '/api/v1/signin'
        self.signup_url = '/api/v1/signup'
        self.quizes_url = '/api/v1/questions'
        self.quiz_url = '/api/v1/question'
        self.answers_url = '/api/v1/question/<int:d>/answers'

        self.question_data = {
            "question_brief": "Meaning of life?",
            "question_description": "Have you ever just wondered what is life?"
        }

        self.answer_data = {
            "answer_body" : "Life is just Divine"
        }

        self.signup_data = {
            "username": "newuser",
            "email": "newuser@company.com",
            "password": "newuserpassword"
        }

        self.signin_data = {
            "email": "newuser@company.com",
            "password": "newuserpassword"
        }




    def tearDown(self):
        self.client = create_app('testing')
        self.mime_type = None
        self.login_url = None
        self.signup_url = None
        self.quizes_url = None
        self.quiz_url = None
        self.answers_url = None
        self.question_data = None
        self.answer_data = None
        self.signup_data = None
        self.signin_data = None