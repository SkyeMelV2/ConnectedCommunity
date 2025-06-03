from flask import Flask, jsonify, request
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

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
    return jsonify(population_data)
    return jsonify(population_data)
@app.route('/api/population/<year>', methods=['GET'])
def get_population_by_year(year):>', methods=['GET'])
    if year in population_data:):
        return jsonify(population_data[year])
    return jsonify({"error": "Year not found"}), 404
    return jsonify({"error": "Year not found"}), 404
@app.route('/api/population/demographics/<year>', methods=['GET'])
def get_demographics_by_year(year):phics/<year>', methods=['GET'])
    if year in population_data:ar):
        return jsonify(population_data[year]['demographics'])
    return jsonify({"error": "Year not found"}), 404aphics'])
    return jsonify({"error": "Year not found"}), 404
@app.route('/api/population/years', methods=['GET'])
def get_available_years():n/years', methods=['GET'])
    return jsonify(list(population_data.keys()))
    return jsonify(list(population_data.keys()))
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))_':

    app.run(debug=True, host='0.0.0.0', port=port)    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)