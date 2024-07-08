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
        Returns:
            True if path requires authentication, False otherwise
        """
        if path is None:
            return True
        if excluded_paths is None or not excluded_paths:
            return True

        # Normalize path to ensure it ends with a slash
        if not path.endswith('/'):
            path += '/'

        # Check if normalized path is in excluded_paths
        for excluded_path in excluded_paths:
            if not excluded_path.endswith('/'):
                excluded_path += '/'

            if path == excluded_path:
                return False

        return True

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
