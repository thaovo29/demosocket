import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect((HOST, PORT))
s.sendall(b"Hello, world")
while True:
    data_len = s.recv(1024)
    s.send("received".encode('utf-8'))
    data_r = s.recv(int(data_len.decode()))
    print(data_r.decode())