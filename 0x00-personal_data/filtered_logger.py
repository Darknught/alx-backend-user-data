#!/usr/bin/env python3
""" Module that returns the log message obfuscated."""
import logging
import re
from typing import List


def filter_datum(
        fields: List[str], redaction: str, message: str, separator: str
        ) -> str:
    """
    Obfuscates specified fields in a log message.

    Args:
        fields (List[str]): List of field names to be obfuscated.
        redaction (str): The string to replace the field values with.
        message (str): The log message containing the fields to be obfuscated.
        separator (str): The character separating different fields
        in the log message.

    Returns:
        str: The log message with specified fields obfuscated.
    """
    return re.sub(
            fr'({"|".join(fields)})=[^{separator}]*',
            lambda match: f"{match.group().split('=')[0]}={redaction}",
            message
    )
