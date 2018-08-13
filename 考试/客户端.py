import socket

sk=socket.socket()
sk.connect(("127.0.0.1",8090))

while 1:
    sk.send(b"hello")
    msg1=sk.recv(1024).decode("utf-8")
    print(msg1)

ck.close()