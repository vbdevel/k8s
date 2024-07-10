import os
import base64

# Генерация случайного ключа размером 32 байта
secret_key = os.urandom(32)
print("Secret key (hex):", secret_key.hex())

# Кодирование ключа в base64
base64_secret_key = base64.b64encode(secret_key).decode('utf-8')
print("Base64 Encoded Key:", base64_secret_key)
