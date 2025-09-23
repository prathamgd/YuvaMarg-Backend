from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# Mock login endpoint
@app.route('/api/login', methods=['POST'])
def login():
    with open('data/login_response.json') as f:
        data = json.load(f)
    return jsonify(data)

# User preferences endpoint
@app.route('/api/preferences', methods=['GET', 'POST'])
def preferences():
    if request.method == 'GET':
        with open('data/user_preferences.json') as f:
            data = json.load(f)
        return jsonify(data)
    elif request.method == 'POST':
        request_data = request.get_json()
        return jsonify({
            "success": True,
            "message": "Preferences updated successfully."
        })

# Mock chatbot gateway endpoint
@app.route('/api/chatbot', methods=['POST'])
def chatbot():
    with open('data/chatbot_response.json') as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
