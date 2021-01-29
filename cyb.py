import requests


ATOM_GCYB_PRICE = 1.485
GCYB_SUPPLY = 1_000_000


def get_data():
    return requests.get('https://api.coingecko.com/api/v3/coins/cosmos').json()


def get_cyb_market_data():
    resp = get_data()
    current_price = get_current_price(resp)['current_price']
    market_cap = get_market_cap(current_price)['market_cap']
    return {
        "market_data": {
            "current_price": current_price,
            "market_cap": market_cap,
            "market_cap_rank": None,
            "price_change_percentage_24h": resp['market_data']["price_change_percentage_24h"],
            "price_change_percentage_7d": resp['market_data']["price_change_percentage_7d"],
            "price_change_percentage_30d": resp['market_data']["price_change_percentage_30d"]
        }
    }

def get_current_price(resp):
    return {
        "current_price": {
            "usd": resp['market_data']["current_price"]['usd'] * ATOM_GCYB_PRICE,
            "btc": resp['market_data']["current_price"]['btc'] * ATOM_GCYB_PRICE,
            "atom": ATOM_GCYB_PRICE,
            "eth": resp['market_data']["current_price"]['eth'] * ATOM_GCYB_PRICE
        }
    }

def get_market_cap(current_price):
    return {
        "market_cap": {
            "usd": current_price["usd"] * GCYB_SUPPLY,
            "btc": current_price["btc"] * GCYB_SUPPLY,
            "atom": current_price["atom"] * GCYB_SUPPLY,
            "eth": current_price["eth"] * GCYB_SUPPLY
        }
    }