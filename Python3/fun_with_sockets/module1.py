import socket
from _thread import *

host = ""
port = 80
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(2)

def send(conn):
    while True:
        conn.send("Hello".encode())

while True:
    conn,addr = s.accept()
    start_new_thread(send,(conn,))
