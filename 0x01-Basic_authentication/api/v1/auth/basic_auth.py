#!/usr/bin/env python3
""" A new class that inherits
"""
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """ class that inherits from Auth
    """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """ A method that returns Base64 part of the
        Authorization header for Basic Authentication
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None

        return authorization_header[len("Basic "):]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """ method that returns decoded value of a Base64 string
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            dcoded_bytes = base64.b64decode(base64_authorization_header)
            return dcoded_bytes.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """ Method that returns the user email and password
        from the Base64 decoded value.
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None

        usr_email, usr_password = decoded_base64_authorization_header.split(
                ':', 1)
        return usr_email, usr_password
