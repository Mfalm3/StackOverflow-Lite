"""Validator Utils."""
import re


def valid_email(email):
    """Email validation function."""
    if re.match('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$', email):
        return True
    return False


def email_exist(email, db):
    """Check if email exists in database."""
    for rows in db:
        if email in rows.values():
            return True
        return False


def username_exists(username, db):
    """Check if username exists in database."""
    for rows in db:
        if username in rows.values():
            return True
        return False
