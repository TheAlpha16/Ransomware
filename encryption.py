from Crypto.Cipher import  AES

key = 'my'


def encrypt(msg):
    cipher = AES.new(key, AES.MODE_CBC)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(msg.encode('ascii'))
    return nonce, ciphertext, tag


def decrypt (nonce, ciphertext, tag):
    cipher = AES.new(key, AES.MODE_CBC, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    try:
        cipher.verify(tag)
        return plaintext.decode('ascii')
    except:
        return False

message = 'hi guys how are you'


if __name__ == "__main__":
    p = encrypt(message)
    print(p)
