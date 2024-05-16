import base64
hex_key = "5e72c5817d44bdd46efc891eff9d0358356540086eae51eea95ef12b83bed8e0"
key_bytes = bytes.fromhex(hex_key)
base64_secret_key = base64.b64encode(key_bytes).decode('utf-8')
print("Base64 Encoded Key:", base64_secret_key)

