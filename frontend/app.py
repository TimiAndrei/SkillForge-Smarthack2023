import json
import requests
from flask import Flask
from flask import render_template

app = Flask(__name__)

headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiZjNhN2U2M2YtOGNmZC00YWU3LWJjNjQtYWU3MGQ5NjQyZjI4IiwidHlwZSI6ImFwaV90b2tlbiJ9.y70icVcF9BQzlWB70xrKTlIosjnF-OqB0etLhmqTdjw"}

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/get-quote")
def getQuote():
    url ="https://api.edenai.run/v2/text/generation"
    payload = {
      "providers": "cohere",
      "text": "Write me a short inspirational quote to make me want to improve my skills",
      "temperature" : 0.9,
      "max_tokens" : 300
    }
 
    response = requests.post(url, json=payload, headers=headers)
    
    result = json.loads(response.text)
    
    print(result['cohere']['generated_text'])

@app.route("/get-skill-suggestion")
def getSkillSuggestion():
    url ="https://api.edenai.run/v2/text/generation"
    payload = {
        "providers": "cohere",
        # TO DO: Gather the user categories and insert them in the query below
        # categories = ""
        # for item in user.getCategories():
        #     categories += item + ", "
        "text": "Show me some learning suggestions based on my needs:" + "" + ". Don't give me details about the suggestions, just the titles.",
        "temperature" : 0.9,
        "max_tokens" : 300
    }
 
    response = requests.post(url, json=payload, headers=headers)
    
    result = json.loads(response.text)
    
    print(result['cohere']['generated_text'])