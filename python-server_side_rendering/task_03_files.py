#!/usr/bin/python3
"""Display product data loaded from JSON or CSV files."""

import csv
import json
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


@app.route("/products")
def products():
    """Render products from the requested source, optionally filtered by ID."""
    source = request.args.get("source")
    if source == "json":
        product_data = read_json_products()
    elif source == "csv":
        product_data = read_csv_products()
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
