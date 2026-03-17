from flask import Flask
import psycopg2
import os
import jsonify

app = Flask(__name__)
database_url = psycopg2.connect(os.getenv("DATABASE_URL"))
cursor = database_url.cursor()

@app.route("/ping")
def ping():
    return "succesful response"

@app.route("/top10")
def top_10():
    cursor.execute("SELECT * FROM scores ORDER BY customers_served DESC LIMIT 10")
    return jsonify(cursor.fetchall())

@app.route("/top5")
def top_5():
    cursor.execute("SELECT * FROM scores ORDER BY customers_served DESC LIMIT 5")
    return jsonify(cursor.fetchall())