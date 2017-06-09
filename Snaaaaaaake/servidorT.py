import socket
import threading

host = "172.16.32.116"
port = 50001

socketito = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketito.bind((host, port))
socketito.listen(1)

def iniciar(*args):
    perrito = args[0]
    addr = args[1]
    try:
        print('conexion con {}.'.format(addr))
        perrito.send("server: Weeena choro".encode('UTF-8'))
        while True:
            datos = perrito.recv(4096)
            if datos:
                print('recibido: {}'.format(datos.decode('utf-8')))
    finally:
        perrito.close()

while 1:
    perrito, addr = socketito.accept()
    threading.Thread(target=iniciar, args=(perrito, addr)).start()
