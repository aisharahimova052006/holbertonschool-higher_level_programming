#!/usr/bin/python3
from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


def read_json_file():
    with open("products.json", "r", encoding="utf-8") as f:
        return json.load(f)


def read_csv_file():
    products = []
    with open("products.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append(row)
    return products


def read_sql_file():
    products = []
    conn = sqlite3.connect("products.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, category, price FROM Products")
    rows = cursor.fetchall()
    conn.close()

    for row in rows:
        products.append({
            "id": row["id"],
            "name": row["name"],
            "category": row["category"],
            "price": row["price"]
        })
    return products


@app.route("/products")
def products():
    source = request.args.get("source")
    product_id = request.args.get("id")

    try:
        if source == "json":
            data = read_json_file()
        elif source == "csv":
            data = read_csv_file()
        elif source == "sql":
            data = read_sql_file()
        else:
            return render_template(
                "product_display.html",
                error="Wrong source",
                products=[]
            )
    except Exception:
        return render_template(
            "product_display.html",
            error="Database error",
            products=[]
        )

    if product_id is not None:
        found = [p for p in data if str(p.get("id")) == product_id]
        if not found:
            return render_template(
                "product_display.html",
                error="Product not found",
                products=[]
            )
        data = found

    return render_template(
        "product_display.html",
        products=data,
        error=None
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)

