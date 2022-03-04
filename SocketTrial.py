import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
print(PORT)
print(SERVER)
ADDR = (SERVER,PORT)
print(ADDR)
server.bind(ADDR)

def handle_client(conn, addr):
    pass

#def start():
    #server.listen()
    #while True:
       # conn, addr = server.accept()
       # print(f"[Active connections]... {conn, addr}")


print('[Starting] Server is starting...')
#start()
 




