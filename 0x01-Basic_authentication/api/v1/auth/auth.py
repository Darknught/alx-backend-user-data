#!/usr/bin/env python3
""" A Method that creates a class Auth."""
from flask import request
from typing import List, TypeVar


class Auth:
    """ Class definition."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ method to require authentication
        Args:
            path - string
            excluded_paths: List of strings
        """
        return False


    def authorization_header(self, request=None) -> str:
        """ Method to handle authorization header
        Args:
            request - None
        Return: string
        """
        return None


    def current_user(self, request=None) -> TypeVar('User'):
        """ A method that determines the current user
        Args:
            request - None
        Return: The user
        """
        return None
