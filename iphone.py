import json

import requests

hive = requests.get('https://prices.splinterlands.com/prices').json()
price_hive = float(hive.get('hive'))

json_data = {
    "jsonrpc": "2.0",
    "id": 1684867140822,
    "method": "find",
    "params": {
        "contract": "market",
        "query": {
            "symbol": "CHAOS"
        },
        "indexes": [
            {
                "index": "priceDec",
                "descending": True
            }
        ],
        "limit": 1000,
        "offset": 0,
        "table": "buyBook"
    }
}
chaos = requests.post('https://enginerpc.com/contracts', json=json_data).json()
chaos_price = float(chaos.get('result')[0].get('price'))

bucks = chaos_price * price_hive

print(f'Цена CHAOS пака: {round(bucks,2)}')
