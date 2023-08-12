from flask_cors import CORS
from flask import Flask, request, jsonify
import pandas as pd

# Load the CSV file
data = pd.read_csv('./phishing-address.csv')


app = Flask(__name__)
CORS(app)


# Set of addresses for O(1) lookup
addresses = set(data.iloc[:, 0].tolist())


@app.route('/check', methods=['POST'])
def check():
    # Extract address from POST data
    address = request.json.get('address')

    # Check if the address is in the set
    if address in addresses:
        return jsonify({"result": "phishing"}), 200
    else:
        return jsonify({"result": "normal"}), 200

# To avoid the typical Flask reloader issue in this environment, we'll use the following function to run the app


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=30328)
