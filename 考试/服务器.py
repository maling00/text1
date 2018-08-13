import socket

sk=socket.socket()
sk.bind(("127.0.0.1",8090))
sk.listen()
conn,addr=sk.accept()

while 1:
    msg1 = conn.recv(1024).decode("utf-8")
    print(msg1)
    msg2 = input(">>>").encode("utf-8")
    conn.send(msg2)

conn.close()
sk.close()



