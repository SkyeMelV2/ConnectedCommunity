from flask import Flask, jsonify, request
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app, resources={
    r"/*": {
        "origins": "*",  # Allow all origins temporarily for testing
        "methods": ["GET", "OPTIONS"],
        "allow_headers": ["Content-Type", "Accept"]
    }
})

# Sample population data
population_data = {
    "2025": {
        "total": 1000000,
        "demographics": {
            "age_0_14": 200000,
            "age_15_64": 650000,
            "age_65_plus": 150000
        }
    },
    "2024": {
        "total": 980000,
        "demographics": {
            "age_0_14": 195000,
            "age_15_64": 640000,
            "age_65_plus": 145000
        }
    }
}

@app.route('/api/population', methods=['GET'])
def get_population():
    return jsonify(population_data)

@app.route('/api/population/<year>', methods=['GET'])
def get_population_by_year(year):
    if year in population_data:
        return jsonify(population_data[year])
    return jsonify({"error": "Year not found"}), 404

@app.route('/api/population/demographics/<year>', methods=['GET'])
def get_demographics_by_year(year):
    if year in population_data:
        return jsonify(population_data[year]['demographics'])
    return jsonify({"error": "Year not found"}), 404

@app.route('/api/population/years', methods=['GET'])
def get_available_years():
    return jsonify(list(population_data.keys()))

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Accept')
    response.headers.add('Access-Control-Allow-Methods', 'GET,OPTIONS')
    return response

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))  # Changed default port to 10000
    app.run(host='0.0.0.0', port=port)  # Removed debug=True for production