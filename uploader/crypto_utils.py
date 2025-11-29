from cryptography.fernet import Fernet
import os

KEY_FILE = "secret.key"

def load_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:
            f.write(key)
    else:
        with open(KEY_FILE, "rb") as f:
            key = f.read()
    return key

FERNET_KEY = load_key()
fernet = Fernet(FERNET_KEY)

def encrypt_file(file_bytes: bytes) -> bytes:
    return fernet.encrypt(file_bytes)

def decrypt_file(encrypted_bytes: bytes) -> bytes:
    return fernet.decrypt(encrypted_bytes)
