#!/usr/bin/python3
"""A Flask application that renders items from a JSON file."""

import json
from pathlib import Path

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/items")
def items():
    """Render the items page using data from items.json."""
    data_path = Path(__file__).with_name("items.json")
    with data_path.open(encoding="utf-8") as file:
        data = json.load(file)
    return render_template("items.html", items=data.get("items", []))


if __name__ == "__main__":
    app.run(debug=True, port=5000)
