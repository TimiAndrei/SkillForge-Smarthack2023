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


def getDB():
    conn = sqlite3.connect('SHDB.db')
    cursor = conn.cursor()
    return conn, cursor


conn = sqlite3.connect('SHDB.db')
cursor = conn.cursor()

currentUser = None

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


@app.route('/api/addSkill', methods=['POST'])
def add_skill():
    try:
        skill_data = request.json

        required_fields = ['name', 'category', 'difficulty',
                           'points', 'approval', 'questLogID']
        for field in required_fields:
            if field not in skill_data:
                return jsonify({'success': False, 'error': f'Missing required field: {field}'}), 400

        conn, cursor = getDB()

        cursor.execute('''INSERT INTO skill (name, category, difficulty, description, deadline, points, approval, questLogID) 
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                       (skill_data['name'], skill_data['category'], skill_data['difficulty'],
                        skill_data.get('description', ''), skill_data.get(
                            'deadline', None),
                        skill_data['points'], skill_data['approval'], skill_data['questLogID']))

        conn.commit()
        conn.close()

        return jsonify({'success': True, 'message': 'Skill added successfully'})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})


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
        global currentUser
        data = request.json
        accountName = data.get("accountName")
        password = data.get("password")
        conn, cursor = getDB()

        cursor.execute(
            "SELECT * FROM user WHERE accountName=?", (accountName,))
        db_user = cursor.fetchone()

        if db_user is not None:
            byte_stored_password = db_user[4]
            stored_password = byte_stored_password.decode('utf-8')
            if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
                currentUser = user(db_user[1], db_user[2], db_user[3], db_user[4], db_user[5], db_user[6],
                                   db_user[7], db_user[8], db_user[9], db_user[10], db_user[11], db_user[12])
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


@app.route('/api/get-user', methods=['GET'])
def getUser():
    return jsonify(currentUser.__dict__)


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
    difficulties = [(quest, quest.getDifficultyPercentages())
                    for quest in quests]

    return difficulties


@app.route('/api/get-points-per-category', methods=['GET'])
def getPointsPerCategory():
    return currentUser.getPointsPerCategory()


@app.route('/api/get-streak', methods=['GET'])
def getStreak():
    print(currentUser.getStreak())
    return [currentUser.getStreak()]
