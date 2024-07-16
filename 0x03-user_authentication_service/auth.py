#!/usr/bin/env python3
""" Module that definesa _hash_password method
"""
import bcrypt
import secrets
from db import DB, User
from sqlalchemy.orm.exc import NoResultFound


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def _hash_password(self, password: str) -> bytes:
        """ Method to return the hashed password
        """
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password

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
        hashed_password = self._hash_password(password)

        # Add the new User object to database
        new_user = self._db.add_user(
                email=email, hashed_password=hashed_password.decode('utf-8'))

        return new_user
