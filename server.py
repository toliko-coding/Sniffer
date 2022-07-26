import socket
import pickle
from time import sleep

localIP = "localhost"
localPort = 12321
bufferSize = 1024
msgFromServer = "Hello UDP Client"
bytesToSend = str.encode(msgFromServer)
d = 3
seqBuff = []


def byte_xor(a1, b1):
    return bytes(a ^ b for a, b in zip(a1, b1))


# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))
print("UDP server up and listening")
UDPServerSocket.settimeout(5)
# Listen for incoming datagrams
while True:
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    unPackedMsg: tuple[bytes, bytes, int] = pickle.loads(message)
    clientMsg = "Message from Client:{}".format(unPackedMsg)
    clientIP = "Client IP Address:{}".format(address)
    print(unPackedMsg)
    print(clientIP)

    # Sending a reply to client
    UDPServerSocket.sendto(bytesToSend, address)

    if unPackedMsg[0].decode() == "Server":
        sleep(5)
    else:
        seqBuff.append(unPackedMsg)

    if len(seqBuff) == 2:
        UDPServerSocket.sendto(b"Resend packet", address)
