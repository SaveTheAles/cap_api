from flask import Flask, jsonify
from cyb import get_cyb_market_data, GCYB_SUPPLY
from gol import get_gol_market_data, GGOL_SUPPLY

app = Flask(__name__)


@app.route('/')
def index():
    return "/api/v3/coins/cyber"


@app.route('/api/v3/coins/cyb', methods=['GET'])
def cyb_data():
    market_data = get_cyb_market_data()['market_data']
    return jsonify({
        "name": "cyber",
        "symbol": "gcyb",
        "image": "https://cyber.page/blue-circle.a8fa89beb0.png",
        "market_data": market_data,
        "supply": GCYB_SUPPLY
    })


@app.route('/api/v3/coins/gol', methods=['GET'])
def gol_data():
    market_data = get_gol_market_data()['market_data']
    return jsonify({
        "name": "euler~Foundation",
        "symbol": "ggol",
        "image": "https://etherscan.io/images/main/empty-token.png",
        "market_data": market_data,
        "supply": GGOL_SUPPLY
    })


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)