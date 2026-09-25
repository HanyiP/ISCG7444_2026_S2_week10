import json
from flask import Flask

# Initialize the Flask application
app = Flask(__name__)

# Define the root route
@app.route("/")
def home():
    return json.dumps({})

@app.route("/test")
def test_api():
    return json.dumps({"message","success"})

# Run the app locally (optional, but convenient for running via 'python app.py')
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)