import socket

host = "172.16.32.116"
port = 50001

socketito = socket.socket()

socketito.connect((host, port))

datitos = socketito.recv(1024)
print (datitos.decode('utf-8'))

while True:
    mensaje = raw_input("envia un mensaje: ")
    socketito.send(mensaje.encode('utf-8'))
    if mensaje == "salir":
        break
        print("chaolin")
        socketito.close()
