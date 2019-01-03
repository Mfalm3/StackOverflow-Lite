"""Tests for Users."""

import json

from app.tests.v1.base_test import BaseTest


class TestUsers(BaseTest):
    """Test class for users."""

    def test_signup(self):
        """Test for signup endpoint."""
        with self.client as c:
            headers = {"Content-Type": self.mime_type}
            signup_data0 = {
                "username": "dev0",
                "email": "dev0@company.com",
                "password": "dev0password"
            }
            signup_response = c.post(self.signup_url, data=json.dumps(signup_data0), headers=headers)
            result = json.loads(signup_response.data.decode('utf-8'))

            self.assertEqual(result["message"], "User created successfully!")
            self.assertEqual(result["status"], "success")
            self.assertEqual(signup_response.status_code, 201)
            # self.assertIn(self.mime_type, signup_response.data)

    def test_signup_username_already_exists(self):
        """Test for signup endpoint with username already existing."""
        with self.client as c:
            headers = {"Content-Type": self.mime_type}
            signup_data1 = {
                "username": "dev",
                "email": "newuser1@company.com",
                "password": "newpassword"
            }
            signup_response = c.post(self.signup_url, data=json.dumps(signup_data1), headers=headers)
            result = json.loads(signup_response.data.decode('utf-8'))
            self.assertEqual(signup_response.status_code, 409)

            self.assertEqual(result["message"], "Username already exists. Please choose another username")
            self.assertEqual(result["status"], "error")
            # self.assertIn(self.mime_type, signup_response.data)

    def test_signup_email_already_exist(self):
        """Test for signup endpoint with email already existing."""
        with self.client as c:
            headers = {"Content-Type": self.mime_type}
            signup_response = c.post(self.signup_url, data=json.dumps(self.signup_data), headers=headers)
            result = json.loads(signup_response.data.decode('utf-8'))
            self.assertEqual(result["message"], "Email already exists! Perhaps you want to login?")

            self.assertEqual(result["status"], "error")
            self.assertEqual(signup_response.status_code, 409)
            # self.assertIn(self.mime_type, signup_response.data.decode('utf-8'))

    def test_signin(self):
        """Test for sign in endpoint."""
        with self.client as c:
            headers = {"Content-Type": self.mime_type}
            signin_response = c.post(self.login_url,  data=json.dumps(self.signin_data), headers=headers)
            result = json.loads(signin_response.data.decode('utf-8'))

            self.assertEqual(result["message"], "User signed in successfully!")
            self.assertEqual(result["status"], "success")
            self.assertEqual(signin_response.status_code, 201)
            # self.assertIn(self.mime_type, signin_response.data.decode('utf-8'))

    def test_signin_with_wrong_credentials(self):
        """Test for sign in with wrong credentials."""
        with self.client as c:
            headers = {"Content-Type": self.mime_type}
            self.signin_data2 = {
                "email": "wrong@email.com",
                "password": "wrong"
            }
        signin_response = c.post(self.login_url, data=json.dumps(self.signin_data2), headers=headers)
        result = json.loads(signin_response.data.decode('utf-8'))

        self.assertEqual(result["status"], "error")
        self.assertEqual(result["message"], "No user found with the given credentials")
        self.assertEqual(signin_response.status_code, 409)
        # self.assertIn(self.mime_type, signin_repsonse.data.decode('utf-8'))
