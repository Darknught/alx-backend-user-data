#!/usr/bin/env python3
""" A function that returns a hashed password."""
import bcrypt


def hash_password(password: str) -> bytes:
    """ Method to hash the password."""
    hashed = bcrypt.hashpw(password.encode('utf-8'),  bcrypt.gensalt())
    return hashed
