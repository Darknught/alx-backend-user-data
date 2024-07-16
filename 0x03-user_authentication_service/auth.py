#!/usr/bin/env python3
""" Module that definesa _hash_password method
"""
import bcrypt
import secrets


def _hash_password(password: str) -> bytes:
    """ Method to return the hashed password
    """
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)
