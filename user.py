import os
import hashlib

def generate_key_pair():
    private_key = os.urandom(128)
    public_key = hashlib.sha256(private_key).digest()
    return private_key, public_key

def register_user(email):
    private_key, public_key = generate_key_pair()
    user_data = {
        'email': email,
        'private_key': private_key,
        'public_key': public_key
    }
    return user_data