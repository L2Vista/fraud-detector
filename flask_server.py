from flask_cors import CORS
from flask import Flask, request, jsonify
import pandas as pd


app = Flask(__name__)
CORS(app)


# Load the CSV file
data = pd.read_csv('./phishing-address.csv', header=None)

# Set of addresses for O(1) lookup
addresses = set(data.iloc[:, 0].tolist())


@app.route('/check', methods=['POST'])
def check():
    # Extract list of address lists from POST data
    lists_of_addresses = request.json.get('lists_of_addresses', [])

    results = []
    for address_list in lists_of_addresses:
        # Check if at least one address in the list is a phishing address
        if any(address in addresses for address in address_list):
            results.append("phishing")
        else:
            results.append("normal")

    return jsonify({"results": results}), 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=30328)
