# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import os, sys, threading

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from socket import *

class Ui_main(QtWidgets.QMainWindow):
    def setupUi(self, main, port, usrname):
        main.setObjectName("main")
        main.setEnabled(True)
        main.resize(640, 443)
        main.setFixedSize(main.width(), main.height())
        main.setMouseTracking(False)
        main.setStyleSheet("QWidget {\n"
"    background-color: #dcdcdc;\n"
"    font-family: \"Noto Serif SC\";\n"
"    font-weight: 500;\n"
"}\n"
"QPushButton {\n"
"    color: #dcdcdc;\n"
"    background-color: #262626;\n"
"    font-family: \"Noto Serif SC\";\n"
"    border-radius: 10px;\n"
"    border: 1px solid #262626;\n"
"}\n"
"QPushButton:hover {\n"
"    color: #dcdcdc;\n"
"    background-color: #3f3f3f;\n"
"    font-family: \"Noto Serif SC\";\n"
"    border: 1px solid #262626;\n"
"}\n"
"QPushButton:pressed {\n"
"    color: #dcdcdc;\n"
"    background-color: #3f3f3f;\n"
"    font-family: \"Noto Serif SC\";\n"
"    border: 1px solid #dcdcdc;\n"
"}\n"
"QToolButton {\n"
"    color: #dcdcdc;\n"
"    background-color: #262626;\n"
"    font-family: \"Noto Serif SC\";\n"
"    border-radius: 10px;\n"
"    border: 1px solid #262626;\n"
"}\n"
"QToolButton:hover {\n"
"    color: #dcdcdc;\n"
"    background-color: #3f3f3f;\n"
"    font-family: \"Noto Serif SC\";\n"
"    border: 1px solid #3f3f3f;\n"
"}\n"
"QToolButton:pressed {\n"
"    color: #dcdcdc;\n"
"    background-color: #3f3f3f;\n"
"    font-family: \"Noto Serif SC\";\n"
"    border: 1px solid #dcdcdc;\n"
"}\n"
"QTextBrowser {\n"
"    background-color: #f5f5f5;\n"
"    color: #262626;\n"
"    border-radius: 10px;\n"
"}\n"
"QLineEdit {\n"
"    background-color: #f5f5f5;\n"
"    color: #262626;\n"
"    text-indent: 10px;\n"
"    border-radius: 10px;\n"
"    padding-left: 10px;\n"
"}\n"
"QGraphicViews {\n"
"    background-image: url(\'./yjs.png\');\n"
"    background-size: 100% 100%;\n"
"}\n"
"QLabel {\n"
"    border-radius: 10px;\n"
"    background-color: #f5f5f5;\n"
"}\n"
"QScrollBar:vertical {\n"
"    width: 10px;\n"
"    border-radius: 5px;\n"
"    border-top-left-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"    background: #f5f5f5;\n"
"    padding-top: 2px;\n"
"    padding-bottom: 2px; \n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: #dcdcdc;\n"
"    width: 8px;\n"
"    border-radius: 4px;\n"
"    margin-left: 0px;\n"
"    margin-right: 2px;\n"
"}\n"
"QGraphicsView {\n"
"    border-image: url(./yjs.png);\n"
# "    background-size: 100% 100%;\n"
"}"
)
        self.sendButton = QtWidgets.QPushButton(main)
        self.sendButton.setGeometry(QtCore.QRect(570, 400, 61, 31))
        self.sendButton.setAutoDefault(False)
        self.sendButton.setDefault(False)
        self.sendButton.setFlat(True)
        self.sendButton.setObjectName("sendButton")
        self.chatMsg = QtWidgets.QTextBrowser(main)
        self.chatMsg.setGeometry(QtCore.QRect(10, 10, 511, 381))
        self.chatMsg.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.chatMsg.setFrameShadow(QtWidgets.QFrame.Plain)
        self.chatMsg.setLineWidth(1)
        self.chatMsg.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.chatMsg.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.chatMsg.setOverwriteMode(True)
        self.chatMsg.setObjectName("chatMsg")
        self.inputMsg = QtWidgets.QLineEdit(main)
        self.inputMsg.setGeometry(QtCore.QRect(10, 400, 551, 31))
        self.inputMsg.setText("")
        self.inputMsg.setFrame(False)
        self.inputMsg.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.inputMsg.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.inputMsg.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.inputMsg.setClearButtonEnabled(False)
        self.inputMsg.setObjectName("inputMsg")
        self.chatroomName = QtWidgets.QLabel(main)
        self.chatroomName.setGeometry(QtCore.QRect(530, 40, 101, 41))
        self.chatroomName.setTextFormat(QtCore.Qt.AutoText)
        self.chatroomName.setAlignment(QtCore.Qt.AlignCenter)
        self.chatroomName.setWordWrap(True)
        self.chatroomName.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.chatroomName.setObjectName(port)
        self.picsButton = QtWidgets.QToolButton(main)
        self.picsButton.setGeometry(QtCore.QRect(530, 330, 31, 22))
        self.picsButton.setObjectName("picsButton")
        self.fileButton = QtWidgets.QToolButton(main)
        self.fileButton.setGeometry(QtCore.QRect(530, 360, 31, 22))
        self.fileButton.setCheckable(False)
        self.fileButton.setChecked(False)
        self.fileButton.setAutoExclusive(False)
        self.fileButton.setObjectName("fileButton")
        self.graphicsView = QtWidgets.QGraphicsView(main)
        self.graphicsView.setGeometry(QtCore.QRect(530, 220, 101, 101))
        self.graphicsView.setAutoFillBackground(False)
        self.graphicsView.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.graphicsView.setFrameShadow(QtWidgets.QFrame.Plain)
        self.graphicsView.setLineWidth(0)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.graphicsView.setBackgroundBrush(brush)
        self.graphicsView.setInteractive(False)
        self.graphicsView.setObjectName("graphicsView")

        self.Name = QtWidgets.QLabel(main)
        self.Name.setGeometry(QtCore.QRect(530, 90, 101, 16))
        self.Name.setAlignment(QtCore.Qt.AlignCenter)
        self.Name.setObjectName("Name")
        self.retranslateUi(main, port, usrname)
        self.sendButton.clicked.connect(self.sendMsg)
        self.picsButton.clicked.connect(self.showPicsMenu)
        self.fileButton.clicked.connect(self.showFileMenu)
        QtCore.QMetaObject.connectSlotsByName(main)

    def retranslateUi(self, main, port, usrname):
        _translate = QtCore.QCoreApplication.translate
        main.setWindowTitle(_translate("main", "Chat Room"))
        self.sendButton.setText(_translate("main", "Send"))
        self.chatMsg.setHtml(_translate("main", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Serif SC\'; font-size:13pt; font-weight:496; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.chatMsg.setPlaceholderText(_translate("main", "Your History Msg HERE."))
        self.inputMsg.setPlaceholderText(_translate("main", "Your Msg HERE."))
        self.chatroomName.setText(_translate("main", port))
        self.picsButton.setText(_translate("main", "Pics"))
        self.fileButton.setText(_translate("main", "File"))
        self.Name.setText(_translate("main", usrname))

    def sendMsg(self):
        # while 1:
        #     try:
        #         yourSentMsg = str(self.inputMsg.text())
        #         if yourSentMsg != 'exit()' and yourSentMsg != '':
        #             self.clientSocket.send(yourSentMsg.encode())
        #         else:
        #             self.clientSocket.close()
        #             break
        #     except ConnectionResetError:
        #         self.clientSocket.close()
        #         break
        # os._exit(0)
        try:
            yourSentMsg = str(self.inputMsg.text())
            if yourSentMsg != 'exit()':
                self.clientSocket.send(yourSentMsg.encode())
                self.inputMsg.setText('')
            else:
                self.clientSocket.close()
        except ConnectionResetError:
            self.clientSocket.close()

    def recvMsg(self):
        while 1:
            try:
                receivedMsg = self.clientSocket.recv(10240)
                if receivedMsg.decode() != '':
                    print(receivedMsg.decode())
                    self.chatMsg.append(receivedMsg.decode())
                    self.chatMsg.moveCursor(-1)
                if len(receivedMsg.decode()) > 5 and receivedMsg.decode()[-2] == 's' and receivedMsg.decode()[-1] == '!':
                    self.Name.setText(str(receivedMsg.decode()).split(' ')[0])
            except ConnectionResetError:
                self.clientSocket.close()
                break
        os._exit(0)

    def showPicsMenu(self):
        QtWidgets.QMessageBox.information(self.picsButton, "pics", "pics")

    def showFileMenu(self):
        QtWidgets.QMessageBox.information(self.fileButton, "file", "file")

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
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    serverPort = int(sys.argv[1])
    mainWindow = QMainWindow()
    ui = Ui_main(serverPort, 'Your Name') # 这里的名字参考生成的py的类名
    # ui.setupUi(mainWindow, 'ChatRoom')
    # mainWindow.show()
    sys.exit(app.exec_())