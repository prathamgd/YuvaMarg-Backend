# 1. Import 'Blueprint' instead of 'Flask'. 'request' is also needed.
from flask import Blueprint, jsonify, request
import json

# 2. CHANGE: Create a Blueprint, not a new Flask app.
# This allows the file to be a modular component.
arjun_bp = Blueprint('arjun_bp', __name__)

# --- 3. CHANGE: Optimize data loading ---
# This helper function reads all the necessary JSON files once.
def load_arjun_data():
    """Loads Arjun's mock data from JSON files into memory."""
    try:
        with open('mock_data/login_response.json', 'r') as f:
            login = json.load(f)
        with open('mock_data/user_preferences.json', 'r') as f:
            preferences = json.load(f)
        with open('mock_data/chatbot_response.json', 'r') as f:
            chatbot = json.load(f)
        return login, preferences, chatbot
    except FileNotFoundError as e:
        # Handle cases where a file might be missing during development
        print(f"ERROR: Missing a mock data file for Arjun's routes: {e}")
        return {}, {}, {}

# This line runs the function once when the server starts, storing the data.
LOGIN_DATA, PREFERENCES_DATA, CHATBOT_DATA = load_arjun_data()


# --- API Endpoints ---

# 4. CHANGE: All routes are now defined on 'arjun_bp', not 'app'.
@arjun_bp.route('/api/login', methods=['POST'])
def login():
    # Now it returns the pre-loaded data, which is much faster.
    return jsonify(LOGIN_DATA)

@arjun_bp.route('/api/preferences', methods=['GET', 'POST'])
def preferences():
    if request.method == 'GET':
        return jsonify(PREFERENCES_DATA)
    elif request.method == 'POST':
        # This part remains the same as it simulates an update.
        request_data = request.get_json()
        return jsonify({
            "success": True,
            "message": "Preferences updated successfully."
        })

@arjun_bp.route('/api/chatbot', methods=['POST'])
def chatbot():
    return jsonify(CHATBOT_DATA)

# 5. CHANGE: Remove the standalone app runner.
# The 'if __name__ == '__main__':' block has been deleted.
# The main.py file is now responsible for running the server.