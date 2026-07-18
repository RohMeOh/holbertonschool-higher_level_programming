#!/usr/bin/python3
"""Display product data from JSON, CSV, or SQLite sources."""

import csv
import json
import os
import sqlite3

from flask import Flask, render_template, request

app = Flask(__name__)


def read_json_file(filename):
    """Read and return products from a JSON file."""
    with open(filename, "r", encoding="utf-8") as json_file:
        return json.load(json_file)


def read_csv_file(filename):
    """Read and return products from a CSV file."""
    products = []

    with open(filename, "r", encoding="utf-8", newline="") as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            products.append({
                "id": int(row["id"]),
                "name": row["name"],
                "category": row["category"],
                "price": float(row["price"])
            })

    return products


def read_sql_file(filename):
    """Read and return products from a SQLite database."""
    products = []

    with sqlite3.connect(filename) as connection:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT id, name, category, price FROM Products"
        )

        for row in cursor.fetchall():
            products.append({
                "id": row[0],
                "name": row[1],
                "category": row[2],
                "price": row[3]
            })

    return products


@app.route("/products")
def products():
    """Display products from the selected data source."""
    source = request.args.get("source")
    product_id = request.args.get("id")

    try:
        if source == "json":
            filename = os.path.join(app.root_path, "products.json")
            product_list = read_json_file(filename)
        elif source == "csv":
            filename = os.path.join(app.root_path, "products.csv")
            product_list = read_csv_file(filename)
        elif source == "sql":
            filename = os.path.join(app.root_path, "products.db")
            product_list = read_sql_file(filename)
        else:
            return render_template(
                "product_display.html",
                products=[],
                error="Wrong source"
            )
    except sqlite3.Error:
        return render_template(
            "product_display.html",
            products=[],
            error="Database error"
        )

    if product_id is not None:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template(
                "product_display.html",
                products=[],
                error="Product not found"
            )

        product_list = [
            product for product in product_list
            if product["id"] == product_id
        ]

        if not product_list:
            return render_template(
                "product_display.html",
                products=[],
                error="Product not found"
            )

    return render_template(
        "product_display.html",
        products=product_list,
        error=None
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)
