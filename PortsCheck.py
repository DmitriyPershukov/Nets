import sys
import socket

myneSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
myneSocket.settimeout(0.5)
try:
    connect = myneSocket.connect(("localhost", 123))
    print('Port :', 2, ' its open.')
    connect.close()
except:
    pass