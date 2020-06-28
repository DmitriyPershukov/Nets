import sys
import socket

def portCheck(port):

    try:
        myneSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        myneSocket.settimeout(0.9)
        connect = myneSocket.connect((hostAdress, port))
        myneSocket.close()
        return f"{port}__open"
    except:
        return f"{port}: closed"

try:
    checkRange = range(int(sys.argv[1]), int(sys.argv[2])+ 1)
    hostAdress =sys.argv[3]

except:
    print("incorrect argumentDa")
    sys.exit(9)

for k in checkRange:
    print(portCheck(k))