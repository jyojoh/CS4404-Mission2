import socket

host = 'localhost'
port = 65000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.bind((host, port))

client.listen(5)

conn, addr = client.accept()
with conn:
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(data.decode())
        data = conn.recv(1024)
