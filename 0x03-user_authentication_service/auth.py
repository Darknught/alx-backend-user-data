#!/usr/bin/env python3
""" Module that definesa _hash_password method
"""
import bcrypt
import secrets
from db import DB, User
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> bytes:
    """ Method to return the hashed password
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Method that takes in str args and return User object
        """
        try:
            # Check if User with this email already exists
            old_user = self._db.find_user_by(email=email)

            if old_user:
                raise ValueError(f"User {email} already exists")
        except NoResultFound:
            pass

        # Hash the password
        hashed_password = _hash_password(password)

        # Add the new User object to database
        new_user = self._db.add_user(
                email=email, hashed_password=hashed_password.decode('utf-8'))

        return new_user

    def valid_login(self, email: str, password: str) -> bool:
        """ Method that locates if the email is valid and decode
        Return:
            True if it matches or False
        """
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode(
                'utf-8'), user.hashed_password.encode('utf-8'))
        except Exception:
            return False

    @staticmethod
    def _generate_uuid(self) -> str:
        """ Method that returns a string representation of new UUID
        """
        return str(uuid.uuid4())
