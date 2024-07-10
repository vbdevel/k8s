import jwt
from jwcrypto import jwk
from time import time

# Загрузка приватного ключа
with open('private_key.json', 'r') as f:
    private_key = jwk.JWK.from_json(f.read())

# Экспорт приватного ключа в формат PEM для библиотеки PyJWT
private_key_pem = private_key.export_to_pem(private_key=True, password=None).decode('utf-8')

# Создание токена
current_time = int(time())
payload = {
    "iss": "http://jwks-svc-cluster",
    "sub": "9l0n0D6s0jl14Zv4Bh5emncpjVNZEhJA@clients",
    "aud": "https://first.wdb.com.ua",
    "iat": current_time,
    "exp": current_time + 7200,
    "gty": "client-credentials",
    "azp": "9l0n0D6s0jl14Zv4Bh5emncpjVNZEhJA",
    "service": "wallet-24.5.0.1"
}

# Получение `kid` из ключа
kid = private_key.thumbprint()
print(kid)
# Подписание токена с использованием приватного ключа и добавлением `kid` в заголовок
token = jwt.encode(payload, private_key_pem, algorithm='RS256', headers={'kid': kid})
print(token)

