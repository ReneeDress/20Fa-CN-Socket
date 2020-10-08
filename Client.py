from socket import *
import threading, os, sys


def recvmsg():
    while 1:
        try:
            receivedMsg = clientSocket.recv(2048)
            if receivedMsg.decode() != '':
                print(receivedMsg.decode())
        except ConnectionResetError:
            clientSocket.close()
            break
    os._exit(0)


def sendmsg():
    while 1:
        try:
            yourSentMsg = input("")
            if yourSentMsg != 'exit()':
                clientSocket.send(yourSentMsg.encode())
            else:
                clientSocket.close()
                break
        except ConnectionResetError:
            clientSocket.close()
            break
    os._exit(0)


if __name__ == '__main__':
    serverName = "localhost"
    serverPort = 9999
    serverPort = int(sys.argv[1])
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    print("The Client is READY to RECEIVE via TCP @", serverPort)
    print(clientSocket)
    threads = [threading.Thread(target=recvmsg), threading.Thread(target=sendmsg)]
    for t in threads:
        t.start()