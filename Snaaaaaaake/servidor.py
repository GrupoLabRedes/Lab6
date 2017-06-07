
import socket

socketito = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketito.bind(("127.0.0.1",50001)) # direccion ip y puerto, solamente asignado
socketito.listen(1)

sock, addr = socketito.accept() # recibira 2 parametros
I=sock.recv(1024)								# recibe 1024 bites de datos, no puede recibir mas

while True:
        perrito = sock.recv(1024)
        print (I + ": " + perrito)
        

sock.close()

s.close()
