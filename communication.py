import hmac
import hashlib
from serpent import serpent_encrypt, serpent_decrypt

def derive_keys(chain_key):
    message_key = hmac.new(chain_key, b'\x01', hashlib.sha256).digest()
    new_chain_key = hmac.new(chain_key, b'\x02', hashlib.sha256).digest()
    return message_key, new_chain_key

class Communication:
    def __init__(self):
        self.chain_key = os.urandom(32)

    def send_message(self, message):
        message_key, self.chain_key = derive_keys(self.chain_key)
        encrypted_message = serpent_encrypt(message, message_key)
        return encrypted_message

    def receive_message(self, encrypted_message):
        message_key, self.chain_key = derive_keys(self.chain_key)
        message = serpent_decrypt(encrypted_message, message_key)
        return message