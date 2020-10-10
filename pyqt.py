import sys, time
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
# 对应之前生成的py文件名
# from gui import *
from guiplus import *
from login import *

class login_Window(Ui_Login):
    def Login(self):
        # admin = [['linyijun', 'linyijun'], ['reneedress', 'reneedress']]
        username = str(self.usr.text())
        password = str(self.pwd.text())
        mainWindow.clientSocket.send(username.encode())
        while 1:
            receivedMsg = mainWindow.clientSocket.recv(20480)
            print('login', receivedMsg.decode())
            # if receivedMsg.decode() == 'Enter your username: ':
            #     mainWindow.clientSocket.send(username)
            if receivedMsg.decode() == 'Enter your password: ':
                mainWindow.clientSocket.send(password.encode())
            elif len(receivedMsg.decode()) > 5 and receivedMsg.decode()[-2] == 's' and receivedMsg.decode()[-1] == '!':
                mainWindow.Name.setText(str(receivedMsg.decode()).split(' ')[0])
                # mainWindow.chatMsg.append('Current DateTime:  ' + time.strftime("%Y/%m/%d %H:%M:%S", time.localtime()))
                mainWindow.chatMsg.append('Welcome ' + username + '!\n================')
                print('accept', mainWindow.clientSocket)
                self.close()
                mainWindow.show()
                break
            else:
                print('reject')
                QtWidgets.QMessageBox.information(self, "Wrong username or password.", "Wrong username or password.")
                break
        # # usrpwd = [username, password]
        # if usrpwd in admin:
        #     # self.setResult(1)
        #     print('accept', mainWindow.clientSocket)
        #     # QtWidgets.QMessageBox.information(self.loginButton, "login", "login")
        #     # print('info done')
        #     # self.accept()
        #     self.close()
        #     mainWindow.show()
        # else:
        #     print('reject')
        #     # self.reject()
        #     # self.setResult(0)

    def __init__(self, port):
        super(Ui_Login, self).__init__()
        self.setupUi(self, port)
        self.retranslateUi(self, port)
        self.show()

class main_Window(Ui_main):
    def __init__(self, serverPort, usrname):
        super(Ui_main, self).__init__()
        serverName = "localhost"
        # serverPort = 9124
        # serverPort = int(sys.argv[1])
        port = "ChatRoom\n" + str(serverPort)
        self.clientSocket = socket(AF_INET, SOCK_STREAM)
        self.clientSocket.connect((serverName, serverPort))
        self.setupUi(self, port, usrname)
        self.retranslateUi(self, port, usrname)
        print("The Client is READY to RECEIVE via TCP @", serverPort)
        print(self.clientSocket)
        threads = [threading.Thread(target=self.recvMsg), threading.Thread(target=self.sendMsg)]
        for t in threads:
            # self.chatMsg.moveToThread(t)
            # self.inputMsg.moveToThread(t)
            t.start()
        # self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    serverPort = int(sys.argv[1])
    mainWindow = main_Window(serverPort, 'Your Name')
    loginWindow = login_Window(serverPort)
    # mainWindow = QApplication()
    # loginWindow = QDialog()
    # ui_main = Ui_main(serverPort, 'Your Name')
    # ui_login = Ui_Login(serverPort)
    # ui.setupUi(mainWindow, 'ChatRoom')
    # mainWindow.show()
    sys.exit(app.exec_())