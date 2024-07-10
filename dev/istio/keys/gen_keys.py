from jwcrypto import jwk
import json

# Генерация ключей
key = jwk.JWK.generate(kty='RSA', size=2048)

# Экспорт приватного ключа в формат JSON
private_key_json = key.export(private_key=True)

# Сохранение приватного ключа в файл
with open('private_key.json', 'w') as private_file:
    private_file.write(private_key_json)

# Экспорт публичного ключа с `kid`
public_key_json = json.loads(key.export(private_key=False))
public_key_json['kid'] = key.thumbprint()

# Создание JWK Set
jwks = {"keys": [public_key_json]}

# Сохранение JWK Set в файл
with open('jwks.json', 'w') as jwks_file:
    jwks_file.write(json.dumps(jwks))

