#!/usr/bin/env python3
""" Module that returns the log message obfuscated."""
import logging
import re
from typing import List, Tuple

PII_FIELDS: Tuple[str, ...] = ("name", "email", "phone", "ssn", "password")


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


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class to filter values in log records
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Initialize the formatter with fields to be obfuscated.

        Args:
            fields (List[str]): List of field names to be obfuscated.
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format the log record, obfuscating specified fields.

        Args:
            record (logging.LogRecord): The log record to be formatted.

        Returns:
            str: The formatted log record with specified fields obfuscated.
        """
        original_message = super(RedactingFormatter, self).format(record)
        return filter_datum(
                self.fields, self.REDACTION, original_message, self.SEPARATOR)


def get_logger() -> logging.Logger:
    """ method takes no args and returns a logging.Logger object.
    """
    logger = logging.getLogger("user_data.")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(list(PII_FIELDS))
    stream_handler.SetFormatter(formatter)

    logger.addHandler(stream_handler)
    return logger