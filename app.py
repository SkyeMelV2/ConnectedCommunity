from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/population', methods=['GET'])
def get_population():
    # Sample data - replace with your actual data
    population_data = {
        "total": 1000000,
        "year": 2025
    }
    return jsonify(population_data)

if __name__ == '__main__':
    app.run(debug=True)