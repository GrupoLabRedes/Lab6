import sys
import socket

socketito = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketito.connect(("127.0.0.1",50001))

i = raw_input("Ingrese nombre: ")
socketito.send(i)

while True:
        perrito = raw_input("Ingrese datos: ")
        socketito.send(perrito)

s.close()
