from socket import *
import threading, time, os, sys, getopt


def intermsg(users, client, username):
    print('User Port: ' + str(client[1]))
    while 1:
        try:
            receivedMsg = users[client].recv(20480)
            now = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime())
            if receivedMsg.decode() != '':
                print(now + " The Server has received '" + receivedMsg.decode() + "' as " + str(client[1]) + "'s message. ")
                recvSentMsg = now + ' ' + username + ': \r\n' + receivedMsg.decode()
                # print(users)
                for u in users.values():
                    u.send(recvSentMsg.encode())
        except ConnectionResetError:
            print(str(client[1]) + ' has exited.')
            if len(users) == 1:
                print(len(users), 'user has connected.')
            else:
                print(len(users), 'users have connected.')
            users.pop(client)
            break


def close():
    while 1:
        cmd = input()
        # print('cmd', cmd)
        if cmd == 'exit()':
            # print('enter')
            for u in users.values():
                u.close()
                # print('close')
            # serverSocket.close()
            # print('bfo break')
            break
    os._exit(0)


def login(clientsocket, client):
    while 1:
        # client = (addr, port)
        print(clientsocket, client)
        # usrAsk = 'Enter your username: '
        # usrAsk = 'Current DateTime:  ' + time.strftime("%Y/%m/%d %H:%M:%S", time.localtime())
        # clientsocket.send(usrAsk.encode())
        usrAns = clientsocket.recv(2048)
        print(usrAns.decode())
        pwdAsk = 'Enter your password: '
        clientsocket.send(pwdAsk.encode())
        pwdAns = clientsocket.recv(2048)
        print(pwdAns.decode())
        usrpwd = [usrAns.decode(), pwdAns.decode()]
        if usrpwd in admin:
            success = usrpwd[0] + ' Login Success!'
            clientsocket.send(success.encode())
            users[client] = clientsocket
            if len(users) == 1:
                print(len(users), 'user has connected.')
            else:
                print(len(users), 'users have connected.')
            break
        else:
            failed = 'Login Failed!'
            clientsocket.send(failed.encode())
    threading.Thread(target=intermsg, args=(users, client, usrAns.decode())).start()


# def login():
#     while 1:
#         # client = (addr, port)
#         print(connectionSocket, clientAddr)
#         usrAsk = 'Enter your username: '
#         connectionSocket.send(usrAsk.encode())
#         usrAns = connectionSocket.recv(2048)
#         print(usrAns.decode())
#         pwdAsk = 'Enter your password: '
#         connectionSocket.send(pwdAsk.encode())
#         pwdAns = connectionSocket.recv(2048)
#         print(pwdAns.decode())
#         usrpwd = [usrAns.decode(), pwdAns.decode()]
#         if usrpwd in admin:
#             success = 'Login Success!'
#             connectionSocket.send(success.encode())
#             users[clientAddr] = connectionSocket
#             if len(users) == 1:
#                 print(len(users), 'user has connected.')
#             else:
#                 print(len(users), 'users have connected.')
#             break
#         else:
#             failed = 'Login Failed!'
#             connectionSocket.send(failed.encode())
#     threading.Thread(target=intermsg, args=(users, clientAddr, usrAns.decode())).start()


if __name__ == '__main__':
    admin = [['linyijun', 'linyijun'], ['reneedress', 'reneedress']]
    users = {}
    serverPort = 9999
    serverPort = int(sys.argv[1])
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('localhost', serverPort))
    serverSocket.listen(50)
    print("The Server is READY to RECEIVE via TCP @", serverPort)
    threading.Thread(target=close).start()
    while 1:
        # print(serverSocket)
        print(threading.active_count())
        connectionSocket, clientAddr = serverSocket.accept()
        print(connectionSocket)
        # users[clientAddr] = connectionSocket
        # threading.Thread(target=login).start()
        threading.Thread(target=login, args=(connectionSocket, clientAddr)).start()
    os._exit(0)