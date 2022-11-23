import socket

host = 'localhost'
port = 65000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((host, port))

server.sendall(b'123456')
