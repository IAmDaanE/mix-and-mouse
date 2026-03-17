from flask import Flask, jsonify, request
import psycopg2
import os

app = Flask(__name__)
database_url = psycopg2.connect(os.getenv("DATABASE_URL"))
cursor = database_url.cursor()

@app.route("/ping")
def ping():
    return "succesful response"

@app.route("/top10")
def top_10():
    cursor.execute("SELECT * FROM scores ORDER BY customers_served DESC LIMIT 10")
    rows = cursor.fetchall()
    result = []
    for row in rows:
        result.append({
            "id": row[0],
            "name": row[1],
            "customers_served": row[2],
            "best_cocktail_value": row[3]
        })
    return jsonify(result)

@app.route("/top5")
def top_5():
    cursor.execute("SELECT * FROM scores ORDER BY customers_served DESC LIMIT 5")
    rows = cursor.fetchall()
    result = []
    for row in rows:
        result.append({
            "id": row[0],
            "name": row[1],
            "customers_served": row[2],
            "best_cocktail_value": row[3]
        })
    return jsonify(result)

@app.route("/post", methods=["POST"])
def post_data():
    cursor.execute("INSERT INTO scores VALUES (%s, %s, %s)", ("kingslayer69", 25000, 250))
    database_url.commit()
    return jsonify({"message": "score saved"}), 201