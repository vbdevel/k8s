import base64

key = "HuOIwCr49ztPNPCOV9dSlO0xlxt0siSyOUT/lVFqSNw="
try:
    base64.b64decode(key)
    print("Valid Base64 key")
except Exception as e:
    print(f"Invalid Base64 key: {e}")

