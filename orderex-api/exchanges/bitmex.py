import requests

class Bitmex:




    def new_order(self, symbol, order_type, side, quantity, price, **kwargs):
        request = {
            'symbol': symbol,
            'order_type': order_type,
            'side': side,
            'quantity': quantity,
            'price': price
        }
    def send_order(self, order):
        # testing for now
        base_URI = 'https://www.bitmex.com/api/v1'
        endpoint = '/trade/bucketed'
        params = {'binSize': '1m', 'symbol': 'XBTUSD', 'count': 300}


        response = requests.get(base_URI + endpoint, params=params, proxies=proxies)
        response = response.json()

        print(response)


exchange = Bitmex()

test = exchange.send_order('test')

print(test)