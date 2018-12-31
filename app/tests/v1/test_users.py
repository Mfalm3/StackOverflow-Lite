"""Tests for Users"""

import json

from .base_test import BaseTest
from app.api.v1.models.users_model import UserModel

class TestUsers(BaseTest):

    def test_signup(self):
        with self.client as c:
            headers = {"Content-Type": self.mime_type}
            signup_response = c.post(self.signup_url, data=self.signup_data, headers=headers)
            result = json.loads(signup_response.data.decode('utf-8'))

            self.assertEqual(result['status'], "success")
            self.assertEqual(result['message'], "User created successfully!")
            self.assertEqual(signup_response.status_code, 201)
            self.assertIn(self.mime_type, signup_response.data)

    def test_username_already_exists(self):
        with self.client as c:
            headers = {"Content-Type": self.mime_type}
            signup_response = c.post(self.signup_url, data=self.signup_data, headers=headers)
            result = json.loads(signup_response.data.decode('utf-8'))

            self.assertEqual(result['status'], "error")
            self.assertEqual(result['message'], "Email already exists! Perhaps you want to login?")
            self.assertEqual(signup_response.status_code, 409)
            self.assertIn(self.mime_type, signup_response.data)

            pass

    def test_email_already_exist(self):
        with self.client as c:
            headers = {"Content-Type": self.mime_type}
            signup_response = c.post(self.signup_url, data=self.signup_data, headers=headers)
            result = json.loads(signup_response)

            self.assertEqual(result['status'], "error")
            self.assertEqual(result['message'], "Email already exists! Perhaps you want to login?")
            self.assertEqual(signup_response.status_code, 409)
            self.assertIn(self.mime_type, signup_response.data.decode('utf-8'))




    def test_signin(self):
        with self.client as c:
            headers = {"Content-Type": self.mime_type}
            signin_response = c.post(self.login_url,  data=self.signin_data, headers=headers)
            result = json.loads(signin_response.data.decode('utf-8'))


            self.assertEqual(result['status'], "success")
            self.assertEqual(result['message'], "User signed in successfully!")
            self.assertEqual(signin_response.status_code, 201)
            self.assertIn(self.mime_type, signin_response)


    def test_signin_with_wrong_credentials(self):
        with self.client as c:
            headers = {"Content-Type": self.mime_type}
            self.signin_data = {
                "username": "wrong",
                "password": "wrong"
            }
        signin_repsonse = c.post(self.login_url, data=self.signin_data, headers=headers)
        result = json.loads(signin_repsonse.data.decode('utf-8'))

        self.assertEqual(result['status'], "success")
        self.assertEqual(result['message'], "User signed in successfully!")
        self.assertEqual(signin_repsonse.status_code, 401)
        self.assertIn(self.mime_type, signin_repsonse)