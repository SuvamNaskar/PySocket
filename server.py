import socket

s = socket.socket()
print("Socket Created")

s.bind(('localhost', 9999))
s.listen(5)
print("Socket is listening")

while True:
    c, addr = s.accept()
    name = c.recv(1024).decode()
    print("Got connection from", addr, name)

    c.send(b"Hello World!")

    c.close()