from flask import request, jsonify
import jwt  # For token generation
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
import jwt
from user import user

app = Flask(__name__)
CORS(app)

currentUser = user('admin', 'admin', 'admin', 'admin', 'admin', 'admin')


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


@app.route("/api/login", methods=["POST"])
def login():
    try:
        data = request.json
        accountName = data.get("accountName")
        password = data.get("password")

        conn, cursor = getDB()

        cursor.execute(
            "SELECT * FROM user WHERE accountName=?", (accountName,))
        user = cursor.fetchone()
        # currentUser = user
        user = list(user)
        currentUser = user(user[1], user[2], user[3], user[4], user[5], user[6], user[7], user[8], user[9], user[10], user[11], user[12], user[13])

        if user is not None:
            byte_stored_password = user[4]
            stored_password = byte_stored_password.decode('utf-8')
            if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
                conn.close()
                return jsonify({"success": True, "message": "Login successful"})

        conn.close()
        return jsonify({"success": False, "error": "Invalid email or password"})

    except Exception as e:
        return jsonify({"success": False, "error": str(e)})


@app.route('/api/logout', methods=['POST'])
def logout():
    global currentUser
    try:
        currentUser = None

        return jsonify({'success': True, 'message': 'Logout successful'})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/get-skills', methods=['GET'])
def getSkills():
    return currentUser.getSkills()

@app.route('/api/get-quests', methods=['GET'])
def getQuests():
    quests = currentUser.getQuests()
    progress = [(quest, quest.getProgress()) for quest in quests]
    return progress

@app.route('/api/get-difficulty-percentages', methods=['GET'])
def getDifficultyPercentages():
    quests = currentUser.getQuests()
    difficulties = [(quest, quest.getDifficultyPercentages()) for quest in quests]

    return difficulties

@app.route('/api/get-points-per-category', methods=['GET'])
def getPointsPerCategory():
    return currentUser.getPointsPerCategory()

@app.route('/api/get-streak', methods=['GET'])
def getStreak():
    print(currentUser.getStreak())
    return [currentUser.getStreak()]