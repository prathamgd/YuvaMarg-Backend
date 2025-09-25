import json
from flask import Blueprint, jsonify

# Create a Blueprint object for Arhan's features
arhan_bp = Blueprint('arhan_bp', __name__)

# Helper function to load Arhan's data
def load_arhan_data():
    with open('mock_data/mock_skills.json', 'r') as f:
        skills = json.load(f)
    with open('mock_data/mock_mentors.json', 'r') as f:
        mentors = json.load(f)
    with open('mock_data/mock_profiles.json', 'r') as f:
        profiles = json.load(f)
    return skills, mentors, profiles

# Load the data once
SKILLS_DATA, MENTORS_DATA, PROFILES_DATA = load_arhan_data()

# Define the API endpoints on the blueprint
@arhan_bp.route('/skills', methods=['GET'])
def get_skills():
    return jsonify(SKILLS_DATA)

@arhan_bp.route('/mentors', methods=['GET'])
def get_mentors():
    return jsonify(MENTORS_DATA)

@arhan_bp.route('/profile/<int:user_id>', methods=['GET'])
def get_profile(user_id):
    profile = next((p for p in PROFILES_DATA if p.get("id") == user_id), None)
    if profile:
        return jsonify(profile)
    else:
        return jsonify({"error": "User profile not found"}), 404