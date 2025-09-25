import json
from flask import Blueprint, jsonify

# Create a Blueprint for DJ's features
dj_bp = Blueprint('dj_bp', __name__)

# Helper function to load DJ's data
def load_dj_data():
    """Loads DJ's mock data from the mock_data folder."""
    try:
        # The path must correctly point to the file
        with open('mock_data/opportunities.json', 'r', encoding='utf-8') as f:
            opportunities = json.load(f)
        return opportunities
    except FileNotFoundError:
        print("ERROR: Could not find 'mock_data/opportunities.json'.")
        return [] # Return an empty list to prevent a server crash

# Load the data once when the server starts
OPPORTUNITIES_DATA = load_dj_data()


# --- API Endpoint ---

@dj_bp.route('/opportunities', methods=['GET'])
def get_opportunities():
    # CHANGE: We now return the entire list directly, as that is the
    # structure of opportunities.json.
    return jsonify(OPPORTUNITIES_DATA)