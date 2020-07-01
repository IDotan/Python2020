import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(('127.0.0.1',59595))

with open("books.xml","rb") as fd:
        toSend = fd.read()
        s.send(toSend)