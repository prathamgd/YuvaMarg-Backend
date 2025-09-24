from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import json
import os

# Create the Flask application instance
app = Flask(__name__, static_folder='.')

# Enable CORS (Cross-Origin Resource Sharing)
# This is crucial for allowing the front-end running on a different origin (e.g., your local machine)
# to access the API.
CORS(app) 

# Define the root route to serve the index.html file
@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

# Define the API endpoint for opportunities
@app.route('/api/opportunities', methods=['GET'])
def get_opportunities():
    try:
        # Construct the full path to the opportunities.json file
        file_path = os.path.join(app.root_path, 'opportunities.json')
        
        # Open and read the JSON file
        with open(file_path, 'r', encoding='utf-8') as f:
            opportunities_data = json.load(f)
        
        # Return the data as a JSON response
        return jsonify(opportunities_data)
        
    except FileNotFoundError:
        # If the file isn't found, return an error message
        return jsonify({"error": "Opportunities data file not found."}), 404

# Run the Flask development server
if __name__ == '__main__':
    app.run(debug=True)