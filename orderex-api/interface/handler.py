from api import secret


def get_api_key(exchange, pin):
    print(secret.keys[exchange])
    if secret.keys[exchange]:
        print(exchange, 'key found.')
        pass
    else:
        print('No key found for', exchange)

