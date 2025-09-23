# --- ADD request TO THIS LINE ---
from flask import Flask, jsonify, request
import json
from collections import Counter

# Create an instance of the Flask class
app = Flask(__name__)

@app.route('/api/quiz', methods=['GET'])
def get_quiz_questions():
    # Open the JSON file
    with open('data/quiz_questions.json', 'r') as file:
        # Load the data from the file into a Python list
        questions = json.load(file)
    
    # Return the data as a JSON response
    return jsonify(questions)

# --- START OF NEW CODE BLOCK ---
@app.route('/api/submit-quiz', methods=['POST'])
def submit_quiz():
    # 1. Get the answers sent by the frontend
    answers = request.get_json()
    if not answers:
        # Handle case where no answers are sent
        return jsonify({"error": "No answers provided"}), 400
    
    # 2. Find the most common answer
    counts = Counter(answers)
    dominant_trait = counts.most_common(1)[0][0]
    
    # 3. Choose the roadmap file based on the result
    # (This is the expanded logic)
    if dominant_trait == 'Creative':
        filepath = 'data/roadmap_creative.json'
    elif dominant_trait == 'Analytical':
        filepath = 'data/roadmap_analytical.json'
    elif dominant_trait == 'Organizational':
        filepath = 'data/roadmap_organizational.json'
    elif dominant_trait == 'Social':
        filepath = 'data/roadmap_social.json'
    elif dominant_trait == 'Practical':
        filepath = 'data/roadmap_practical.json'
    else:
        # A default fallback just in case
        filepath = 'data/roadmap_creative.json'
        
    # 4. Load the roadmap data and return it
    with open(filepath, 'r') as file:
        roadmap = json.load(file)
    
    return jsonify(roadmap)
# --- END OF NEW CODE BLOCK ---


# This block allows us to run the app directly from the command line
if __name__ == '__main__':
    # debug=True will automatically restart the server when you save the file
    app.run(debug=True)