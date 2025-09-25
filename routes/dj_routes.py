from flask import Blueprint, jsonify
import json
import os

# Create a Blueprint object for DJ's features
dj_bp = Blueprint('dj_bp', __name__)

# Define the API endpoint for opportunities
@dj_bp.route('/opportunities', methods=['GET'])
def get_opportunities():
    try:
        # Construct the full path to the opportunities.json file
        file_path = os.path.join(os.path.dirname(__file__), '..', 'opportunities.json')
        
        # Open and read the JSON file
        with open(file_path, 'r', encoding='utf-8') as f:
            opportunities_data = json.load(f)
        
        # Return the data as a JSON response
        return jsonify(opportunities_data)
        
    except FileNotFoundError:
        # If the file is not found, return a 404 error
        return jsonify({"error": "Opportunities data file not found."}), 404