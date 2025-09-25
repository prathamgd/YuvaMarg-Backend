import json
from flask import Blueprint, jsonify

# Create a Blueprint object for DJ's features
dj_bp = Blueprint('dj_bp', __name__)

# --- 1. CHANGE: Data loading is now in a clean helper function ---
def load_dj_data():
    """Loads DJ's mock data from the mock_data folder."""
    try:
        # --- 2. CHANGE: The file path now correctly points to 'mock_data/opportunities.json' ---
        with open('mock_data/opportunities.json', 'r', encoding='utf-8') as f:
            opportunities = json.load(f)
        return opportunities
    except FileNotFoundError:
        print("ERROR: Could not find 'mock_data/opportunities.json'. Make sure the file exists.")
        return {} # Return an empty dictionary to prevent a server crash

# Load the data once when the server starts for better performance
OPPORTUNITIES_DATA = load_dj_data()


# --- API Endpoint ---

@dj_bp.route('/opportunities', methods=['GET'])
def get_opportunities():
    # 3. CHANGE: Return the list of scholarships from within the loaded JSON data.
    # The .get() method safely handles cases where the "scholarships" key might be missing.
    return jsonify(OPPORTUNITIES_DATA.get("scholarships", []))