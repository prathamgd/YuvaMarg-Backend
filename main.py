import sys
import os

# --- Start of Diagnostic Code ---
print("--- DIAGNOSTIC INFORMATION ---")
print(f"Current Working Directory: {os.getcwd()}")
print("\nPython's System Path (where it looks for modules):")
for path in sys.path:
    print(f"  -> {path}")
print("----------------------------\n")
# --- End of Diagnostic Code ---


from flask import Flask, jsonify
from flask_cors import CORS

# ... (the rest of your main.py code) ...
from routes.arjun_routes import arjun_bp

from flask import Flask, jsonify
from flask_cors import CORS

# Import the blueprints from your team's route files
from routes.arhan_routes import arhan_bp
from routes.arjun_routes import arjun_bp
from routes.amo_routes import amo_bp
from routes.aryan_routes import aryan_bp
from routes.dj_routes import dj_bp

app = Flask(__name__)
CORS(app)

# Register all the blueprints with the main Flask app
app.register_blueprint(arhan_bp)
app.register_blueprint(arjun_bp)
app.register_blueprint(amo_bp)
app.register_blueprint(aryan_bp)
app.register_blueprint(dj_bp)

# A simple root route to confirm the server is running
@app.route('/', methods=['GET'])
def index():
    return jsonify({"message": "Welcome to the Yuva Marg Backend API!"})

# This part allows you to run the app directly
if __name__ == '__main__':
    app.run(debug=True)