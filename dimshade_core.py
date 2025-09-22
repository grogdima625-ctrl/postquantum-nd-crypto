import numpy as np
import hashlib
import base64
from cryptography.fernet import Fernet

def generate_SO5_key():
    A = np.random.randn(5, 5)
    Q, R = np.linalg.qr(A)
    if np.linalg.det(Q) < 0:
        Q[:, 0] *= -1
    return Q

def derive_scalar_secret(A, B, v):
    v = v / np.linalg.norm(v)
    mixed = (A + B) @ v
    return np.dot(v, mixed)

def scalar_to_key(scalar):
    scalar_bytes = str(scalar).encode()
    key_material = hashlib.sha256(scalar_bytes).digest()
    return base64.urlsafe_b64encode(key_material)

def encrypt(message, scalar):
    key = scalar_to_key(scalar)
    cipher = Fernet(key)
    return cipher.encrypt(message.encode())

def decrypt(token, scalar):
    key = scalar_to_key(scalar)
    cipher = Fernet(key)
    return cipher.decrypt(token).decode()
