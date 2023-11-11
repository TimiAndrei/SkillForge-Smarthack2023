import json
import requests
from flask import Flask
from flask import make_response
from flask import jsonify
from flask import render_template
from flask import request
from flask_cors import CORS
import bcrypt
import sqlite3

app = Flask(__name__)
CORS(app)


def getDB():
    conn = sqlite3.connect('SHDB.db')
    cursor = conn.cursor()
    return conn, cursor


conn = sqlite3.connect('SHDB.db')
cursor = conn.cursor()

headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiZjNhN2U2M2YtOGNmZC00YWU3LWJjNjQtYWU3MGQ5NjQyZjI4IiwidHlwZSI6ImFwaV90b2tlbiJ9.y70icVcF9BQzlWB70xrKTlIosjnF-OqB0etLhmqTdjw"}


@app.route("/api/get-quote")
def getQuote():
    url = "https://api.edenai.run/v2/text/generation"
    payload = {
        "providers": "cohere",
        "text": "Write me a short inspirational quote to make me want to improve my skills",
        "temperature": 0.9,
        "max_tokens": 300
    }

    response = requests.post(url, json=payload, headers=headers)

    result = json.loads(response.text)

    print(result['cohere']['generated_text'])
    return result['cohere']['generated_text']


@app.route("/get-skill-suggestion")
def getSkillSuggestion():
    url = "https://api.edenai.run/v2/text/generation"
    payload = {
        "providers": "cohere",
        # TO DO: Gather the user categories and insert them in the query below
        # categories = ""
        # for item in user.getCategories():
        #     categories += item + ", "
        "text": "Show me some learning suggestions based on my needs:" + "" + ". Don't give me details about the suggestions, just the titles.",
        "temperature": 0.9,
        "max_tokens": 300
    }

    response = requests.post(url, json=payload, headers=headers)

    result = json.loads(response.text)

    print(result['cohere']['generated_text'])
    return result['cohere']['generated_text']


@app.route("/api/test", methods=["GET"])
def test():
    data = {
        "name": "John Doe",
        "level": 1,
        "picture": "idk"
    }
    return data


@app.route("/api/register", methods=["POST"])
def register_user():
    try:
        data = request.json
        email = data.get("email")
        account_name = data.get("accountName")
        password = data.get("password")
        first_name = data.get("firstName")
        last_name = data.get("lastName")
        organization = data.get("organization")
        print(f"Received data: {data}")
        hashed_password = bcrypt.hashpw(
            password.encode('utf-8'), bcrypt.gensalt())

        conn, cursor = getDB()
        cursor.execute('''INSERT INTO user (firstName, lastName, accountName, email, password, organization) VALUES (?, ?, ?, ?, ?, ?)''',
                       (first_name, last_name, account_name, email, hashed_password, organization))
        conn.commit()
        conn.close()

        return jsonify({"success": True, "message": "User registered successfully"})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})
