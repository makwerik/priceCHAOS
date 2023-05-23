import json

import requests

hive = requests.get('https://prices.splinterlands.com/prices').json()
price_hive = float(hive.get('hive'))

chaos = requests.post('https://enginerpc.com/contracts', json=json.load(open('chaos.json', 'r'))).json()
chaos_price = float(chaos.get('result')[0].get('price'))

bucks = chaos_price * price_hive

print(f'Цена CHAOS пака: {round(bucks,2)}')
