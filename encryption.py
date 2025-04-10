from Crypto.Cipher import AES
import base64
import os

# Generate a random 16-byte secret key (store securely in real applications)
SECRET_KEY = os.urandom(16)

def pad_message(message):
    """Ensure message length is a multiple of 16 bytes by padding."""
    return message + (16 - len(message) % 16) * chr(16 - len(message) % 16)

def unpad_message(message):
    """Remove padding after decryption."""
    return message[:-ord(message[-1])]

def encrypt_message(message):
    """Encrypt the message using AES."""
    cipher = AES.new(SECRET_KEY, AES.MODE_ECB)
    encrypted_text = cipher.encrypt(pad_message(message).encode('utf-8'))
    return base64.b64encode(encrypted_text).decode('utf-8')

def decrypt_message(encrypted_message):
    """Decrypt the message using AES."""
    cipher = AES.new(SECRET_KEY, AES.MODE_ECB)
    decrypted_text = cipher.decrypt(base64.b64decode(encrypted_message)).decode('utf-8')
    return unpad_message(decrypted_text)

# Test encryption
if __name__ == "__main__":
    msg = "Hello, Secure Chat!"
    enc = encrypt_message(msg)
    print(f"Encrypted: {enc}")
    dec = decrypt_message(enc)
    print(f"Decrypted: {dec}")
