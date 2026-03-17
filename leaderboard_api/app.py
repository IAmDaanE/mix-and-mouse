from flask import Flask
import psycopg2
import os

app = Flask(__name__)
database_url = psycopg2.connect(os.getenv("DATABASE_URL"))
cursor = database_url.cursor()

@app.route("/ping")
def ping():
    return "succesful response"

@app.route("/winner")
def top_player():
    cursor.execute("SELECT * FROM scores ORDER BY customers_served DESC LIMIT 1")
    return cursor.fetchall()