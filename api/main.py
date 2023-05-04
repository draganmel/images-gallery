"""
This module provides a Flask API endpoint for retrieving a random image from Unsplash 
based on the provided query.

The API uses the Unsplash API and requires an API key, which should be provided in a 
.env.local file.

Example:
    To retrieve a random image of a cat, make a GET request to /new-image?query=cat.

    The response will be a JSON object representing the image metadata.

"""

import os
import requests
from flask import Flask, request
from dotenv import load_dotenv
from flask_cors import CORS

load_dotenv(dotenv_path="./.env.local")


UNSPLASH_URL = "https://api.unsplash.com/photos/random"
UNSPLASH_KEY = os.environ.get("UNSPLASH_KEY", "")
DEBUG = bool(os.environ.get("DEBUG", True))

if not UNSPLASH_KEY:
    raise EnvironmentError(
        "Please create .env.local file and insert there UNSPLASH_KEY"
    )

app = Flask(__name__)
CORS(app)

app.config["DEBUG"] = DEBUG


@app.route("/new-image")
def new_image():
    """
    Get a new image from Unsplash API based on the provided query.

    Returns:
    dict: A dictionary representing the image metadata.
    """
    word = request.args.get("query")

    headers = {"Accept-Version": "v1", "Authorization": "Client-ID " + UNSPLASH_KEY}
    params = {"query": word}
    response = requests.get(
        url=UNSPLASH_URL, headers=headers, params=params, timeout=10
    )

    data = response.json()
    return data


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
