import socket
import json
HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
conn, addr = s.accept()

while True:
    data = conn.recv(1024)
    if not data:
        break
    re_dat = json.dumps({"name":"huydeptrai","2":"huy sieu dep trai"})
    print(len(re_dat))
    conn.sendall(str(len(re_dat)).encode("utf-8"))
    resp = conn.recv(1024)
    print(resp)
    conn.sendall(bytes(re_dat,encoding='utf-8'))
