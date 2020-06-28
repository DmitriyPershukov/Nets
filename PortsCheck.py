import sys
import socket

def portsCheck(port):

    try:
        myneSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        myneSocket.settimeout(0.5)
        connect = myneSocket.connect(("localhost", 123))

        myneSocket.close()
        return f"{port}closed"
    except:
        return f"{port}closed"

try:
    poRange = range(int(sys.), int(sys.argv[2]))