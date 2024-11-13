from flask import Flask, jsonify
from backend.data_processing import load_data

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World! Welcome to Diabeedoc!"

@app.route('/get_food_data')
def get_food_data():
    data = load_data()
    if data is not None:
        # Convert DataFrame to a dictionary
        return jsonify(data.to_dict(orient='records'))
    else:
        return "Data not available", 404

if __name__ == "__main__":
    app.run(debug=True)