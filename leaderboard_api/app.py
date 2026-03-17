from flask import Flask
import psycopg2
import os

app = Flask(__name__)
database_url = psycopg2.connect(os.getenv("DATABASE_URL"))

@app.route("/ping")
def ping():
    return "succesful response"

@app.route("/database_url")
def display_url():
    return str(database_url)