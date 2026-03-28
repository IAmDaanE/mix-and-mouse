from flask import Flask, jsonify, request, render_template
import psycopg2
import os

app = Flask(__name__)
def get_db():
    database_url = psycopg2.connect(os.getenv("DATABASE_URL"))
    return database_url

@app.route("/html")
def html():
    return render_template("testing.html")

@app.route("/wakeup")
def wakeup():
    return "im awake gng"

@app.route("/top10")
def top_10():
    conn = get_db()
    cursor = conn.cursor()
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
    conn.close()
    return jsonify(result)

@app.route("/top5")
def top_5():
    conn = get_db()
    cursor = conn.cursor()
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
    conn.close()
    return jsonify(result)

@app.route("/initial_post", methods=["POST"])
def post_data():
    conn = get_db()
    cursor = conn.cursor()
    data = request.json
    name = data["name"]
    customers_served = data["customers_served"]
    best_cocktail_value = data["best_cocktail_value"]
    cursor.execute("INSERT INTO scores (name, customers_served, best_cocktail_value) VALUES (%s, %s, %s)", (name, customers_served, best_cocktail_value))
    conn.commit()
    conn.close()
    return jsonify({"message": "score saved"}), 201

@app.route("/update_post", methods=["POST"])
def update_data():
    conn = get_db()
    cursor = conn.cursor()
    data = request.json
    name = data["name"]
    customers_served = data["customers_served"]
    best_cocktail_value = data["best_cocktail_value"]
    cursor.execute("UPDATE scores SET customers_served = %s, best_cocktail_value = %s WHERE name = %s",(customers_served, best_cocktail_value, name))
    conn.commit()
    conn.close()
    return jsonify({"message": "score saved"}), 200

@app.route("/full")
def full_database():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM scores")
    response = cursor.fetchall()
    conn.close()
    return jsonify(response)

@app.route("/best_recipe")
def best_recipe():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT name, best_cocktail_value FROM scores ORDER BY best_cocktail_value DESC LIMIT 1")
    response = cursor.fetchall()
    conn.close()
    return response