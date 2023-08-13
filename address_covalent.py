from flask_cors import CORS
from flask import Flask, jsonify, request
import requests


app = Flask(__name__)
CORS(app)


EXTERNAL_SERVER = "http://147.46.116.89:3000"


def fetch_txs_from_address(address):
    response = requests.get(f"{EXTERNAL_SERVER}/mytx?address={address}")
    if response.status_code == 200:
        return response.json()
    return None


def fetch_tx_details(tx_hash):
    response = requests.get(f"{EXTERNAL_SERVER}/tx?amount=1&skip=0&hash={tx_hash}")
    if response.status_code == 200:
        return response.json()
    return None


@app.route('/mytxs', methods=['GET'])
def mytxs():
    address = request.args.get('address')
    amount = int(request.args.get('amount', 0))
    skip = int(request.args.get('skip', 0))

    # Fetch transactions based on address
    tx_data_per_chain = fetch_txs_from_address(address)
    print(len(tx_data_per_chain['data']))

    skip_amount = 0
    # tx_hashes = []
    tx_details_list = []
    for i in range(len(tx_data_per_chain['data'])):
        for item in tx_data_per_chain['data'][i]['data']['items']:
            tx_hash = item['tx_hash']
            # tx_hashes.append(tx_hash)
            detail = fetch_tx_details(tx_hash)['data']['txRequested']
            # print(detail)
            if len(detail) != 0:
                if skip_amount < skip:
                    skip_amount += 1
                else:
                    tx_details_list.append(detail[0])
                    if len(tx_details_list) == amount:
                        response_data = {
                            "status": True,
                            "data": {
                                "txRequested": tx_details_list
                            }
                        }
                        return jsonify(response_data)

    response_data = {
        "status": True,
        "data": {
            "txRequested": tx_details_list
        }
    }
    return jsonify(response_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=30329)
