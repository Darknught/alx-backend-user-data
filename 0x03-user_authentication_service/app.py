#!/usr/bin/env python3
""" Module that defines a flask app
"""
from flask import jsonify


app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def home() -> str:
    """ GET /
    Return:
        Json payload
    """
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
