from flask import Flask, jsonify
from flask_cors import CORS

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
def get_population():
    return jsonify(population_data)

@app.route('/api/population/<year>', methods=['GET'])
def get_population_by_year(year):
    if year in population_data:
        return jsonify(population_data[year])
    return jsonify({"error": "Year not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)