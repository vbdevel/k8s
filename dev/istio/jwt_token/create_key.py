import os
secret_key = os.urandom(32)  # Генерация случайного ключа размером 32 байта
print("Secret key:", secret_key.hex())  # Печать ключа в шестнадцатеричном виде для удобства использования

