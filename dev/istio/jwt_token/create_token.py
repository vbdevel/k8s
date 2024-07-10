import jwt
import datetime

hex_key = "5e72c5817d44bdd46efc891eff9d0358356540086eae51eea95ef12b83bed8e0"
key_bytes = bytes.fromhex(hex_key)

# Информация для вставки в токен.
payload = {
    "iss": "https://auth.wdb.com.ua",  # Эмитент токена
    "sub": "1234567890",   # Идентификатор пользователя
    "service-name": "second", # Имя сервиса для маршрутизации
    "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=600)  # Срок действия токена
}

# Создание токена
token = jwt.encode(payload, key_bytes, algorithm="HS256")
print(token)

