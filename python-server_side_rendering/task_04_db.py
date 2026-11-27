#!/usr/bin/python3
"""Display products loaded from JSON, CSV, or a SQLite database."""

import csv
import json
import sqlite3
from contextlib import closing
from pathlib import Path

from flask import Flask, render_template, request

app = Flask(__name__)


def read_json_products():
    """Read products from products.json."""
    data_path = Path(__file__).with_name("products.json")
    with data_path.open(encoding="utf-8") as file:
        return json.load(file)


def read_csv_products():
    """Read products from products.csv."""
    data_path = Path(__file__).with_name("products.csv")
    with data_path.open(newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def read_sql_products():
    """Read products from the Products table in products.db."""
    data_path = Path(__file__).with_name("products.db")
    with closing(sqlite3.connect(data_path)) as connection:
        connection.row_factory = sqlite3.Row
        rows = connection.execute(
            "SELECT id, name, category, price FROM Products"
        ).fetchall()
    return [dict(row) for row in rows]


@app.route("/products")
def products():
    """Render products from the selected source, optionally filtered by ID."""
    source = request.args.get("source")
    if source == "json":
        product_data = read_json_products()
    elif source == "csv":
        product_data = read_csv_products()
    elif source == "sql":
        try:
            product_data = read_sql_products()
        except sqlite3.Error:
            app.logger.exception("Failed to read products from SQLite database")
            return render_template(
                "product_display.html", products=[], error="Database error"
            )
    else:
        return render_template(
            "product_display.html", products=[], error="Wrong source"
        )

    product_id = request.args.get("id")
    if product_id is not None:
        product_data = [
            product for product in product_data
            if str(product.get("id")) == product_id
        ]
        if not product_data:
            return render_template(
                "product_display.html",
                products=[],
                error="Product not found",
            )

    return render_template(
        "product_display.html", products=product_data, error=None
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)
