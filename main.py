from flask import Flask, jsonify
import json

app = Flask(__name__)

# Load data from the mock JSON files
with open('careers.json') as f:
    careers_data = json.load(f)

with open('colleges.json') as f:
    colleges_data = json.load(f)

@app.route('/careers', methods=['GET'])
def get_careers():
    """
    Serves the mock data for all careers.
    URL: GET /careers
    Expected output: A JSON list of all careers.
    """
    return jsonify(careers_data)

@app.route('/colleges', methods=['GET'])
def get_colleges():
    """
    Serves the mock data for all colleges.
    URL: GET /colleges
    Expected output: A JSON list of all colleges.
    """
    return jsonify(colleges_data)

@app.route('/careers/<int:career_id>', methods=['GET'])
def get_career_by_id(career_id):
    """
    Finds and returns a single career by its ID.
    URL: GET /careers/<career_id>
    Expected output: A single career object in JSON format.
    """
    career = next((c for c in careers_data if c['id'] == career_id), None)
    if career:
        return jsonify(career)
    return jsonify({"error": "Career not found"}), 404

@app.route('/colleges/<int:college_id>', methods=['GET'])
def get_college_by_id(college_id):
    """
    Finds and returns a single college by its ID.
    URL: GET /colleges/<college_id>
    Expected output: A single college object in JSON format.
    """
    college = next((c for c in colleges_data if c['id'] == college_id), None)
    if college:
        return jsonify(college)
    return jsonify({"error": "College not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
