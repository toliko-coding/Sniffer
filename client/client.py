from functools import reduce
import socket
import pickle
from time import sleep

msgFromClient = "Hello UDP Server"
msgFromClientBytes = list(map(lambda x: x.encode(), msgFromClient.split()))
serverAddressPort = ("localhost", 12321)
bufferSize = 1024
d = 3


# XOR function
def byte_xor(a1, b1):
    return bytes(a ^ b for a, b in zip(a1, b1))


# Calculating e
e = reduce(lambda a, b: byte_xor(a, b), msgFromClientBytes)

# Create a UDP socket at client side

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
print("UDP client sending data")

# Send to server using created UDP socket

for i in msgFromClientBytes:
    data = pickle.dumps((i, e, d))
    UDPClientSocket.sendto(data, serverAddressPort)
    msgFromServer = UDPClientSocket.recvfrom(bufferSize)
    msg = "Message from Server {}".format(msgFromServer[0])

    print(msg)
    sleep(3)

UDPClientSocket.close()
