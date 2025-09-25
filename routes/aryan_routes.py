import json
from flask import Blueprint, jsonify

# Create a Blueprint object for Aryan's features
aryan_bp = Blueprint('aryan_bp', __name__)

# --- 1. CHANGE: Data loading is now inside a clean helper function ---
def load_aryan_data():
    """Loads Aryan's mock data from the mock_data folder."""
    try:
        # --- 2. CHANGE: Corrected file paths to include 'mock_data/' ---
        with open('mock_data/careers.json', 'r') as f:
            careers = json.load(f)
        with open('mock_data/colleges.json', 'r') as f:
            colleges = json.load(f)
        return careers, colleges
    except FileNotFoundError as e:
        print(f"ERROR: A data file for Aryan's routes is missing: {e}")
        return [], [] # Return empty lists to prevent a server crash

# Load the data once when the server starts
CAREERS_DATA, COLLEGES_DATA = load_aryan_data()


# --- API Endpoints ---

@aryan_bp.route('/careers', methods=['GET'])
def get_careers():
    return jsonify(CAREERS_DATA)

@aryan_bp.route('/colleges', methods=['GET'])
def get_colleges():
    return jsonify(COLLEGES_DATA)

# --- 3. CHANGE: Changed route parameter from <int:career_id> to <string:career_id> ---
# This allows you to look up careers by names like "software-engineer"
@aryan_bp.route('/careers/<string:career_id>', methods=['GET'])
def get_career_by_id(career_id):
    career = next((c for c in CAREERS_DATA if c.get('id') == career_id), None)
    if career:
        return jsonify(career)
    return jsonify({"error": f"Career with ID '{career_id}' not found"}), 404

# Assuming college IDs are also strings or could be in the future.
# It's safer to use <string> unless you are certain they are integers.
@aryan_bp.route('/colleges/<string:college_id>', methods=['GET'])
def get_college_by_id(college_id):
    # Using .get('id') is safer in case a record is missing an 'id' field
    college = next((c for c in COLLEGES_DATA if str(c.get('id')) == college_id), None)
    if college:
        return jsonify(college)
    return jsonify({"error": f"College with ID '{college_id}' not found"}), 404