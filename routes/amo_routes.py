from flask import Blueprint, jsonify, request
import json
from collections import Counter
import os

# Create a Blueprint object for your features
amo_bp = Blueprint('amo_bp', __name__)

# --- Helper function to get the correct file path ---
def get_data_path(filename):
    # This creates a path like '.../YuvaMarg-Backend/data/filename.json'
    # It's a reliable way to open files in Flask
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    return os.path.join(base_dir, 'data', filename)

# --- Your Quiz Questions Endpoint ---
@amo_bp.route('/quiz', methods=['GET'])
def get_quiz_questions():
    filepath = get_data_path('quiz_questions.json')
    with open(filepath, 'r') as file:
        questions = json.load(file)
    return jsonify(questions)

# --- Your Quiz Submission Endpoint ---
@amo_bp.route('/submit-quiz', methods=['POST'])
def submit_quiz():
    answers = request.get_json()
    if not answers:
        return jsonify({"error": "No answers provided"}), 400
    
    counts = Counter(answers)
    dominant_trait = counts.most_common(1)[0][0]
    
    # Map the trait to the correct filename
    roadmap_files = {
        'Creative': 'roadmap_creative.json',
        'Analytical': 'roadmap_analytical.json',
        'Organizational': 'roadmap_organizational.json',
        'Social': 'roadmap_social.json',
        'Practical': 'roadmap_practical.json'
    }
    
    # Get the filename, with a fallback to 'creative'
    filename = roadmap_files.get(dominant_trait, 'roadmap_creative.json')
    filepath = get_data_path(filename)
        
    with open(filepath, 'r') as file:
        roadmap = json.load(file)
    
    return jsonify(roadmap)  