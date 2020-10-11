# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog

class Ui_Login(QtWidgets.QDialog):
    def setupUi(self, Login, serverPort):
        Login.setObjectName("Login")
        Login.resize(276, 300)
        Login.setFixedSize(Login.width(), Login.height())
        Login.setStyleSheet("QWidget {\n"
"    background-color: #dcdcdc;\n"
"    font-family: \"Noto Serif SC\";\n"
"    font-weight: 500;\n"
"    color: #262626;\n"
"}\n"
"QLineEdit {\n"
"    background-color: #f5f5f5;\n"
"    border-radius: 10px;\n"
"    padding-left: 10px;\n"
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
"QGraphicsView {\n"
"    border-image: url(./yjs.png);\n"
"}"
)
        self.usr = QtWidgets.QLineEdit(Login)
        self.usr.setGeometry(QtCore.QRect(30, 110, 161, 31))
        self.usr.setFrame(False)
        self.usr.setObjectName("usr")
        self.pwd = QtWidgets.QLineEdit(Login)
        self.pwd.setGeometry(QtCore.QRect(30, 160, 161, 31))
        self.pwd.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.pwd.setInputMask("")
        self.pwd.setFrame(False)
        self.pwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pwd.setReadOnly(False)
        self.pwd.setObjectName("pwd")
        self.loginButton = QtWidgets.QPushButton(Login)
        self.loginButton.setGeometry(QtCore.QRect(30, 210, 61, 32))
        self.loginButton.setObjectName("loginButton")
        self.graphicsView = QtWidgets.QGraphicsView(Login)
        self.graphicsView.setGeometry(QtCore.QRect(210, 230, 61, 61))
        self.graphicsView.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.graphicsView.setFrameShadow(QtWidgets.QFrame.Plain)
        self.graphicsView.setLineWidth(0)
        self.graphicsView.setObjectName("graphicsView")
        self.port = QtWidgets.QLineEdit(Login)
        self.port.setGeometry(QtCore.QRect(30, 60, 161, 31))
        self.port.setObjectName("port")
        self.port.setValidator(QIntValidator(8888,65535))
        self.port.setText(str(serverPort))
        self.port.setEnabled(False)
        self.retranslateUi(Login, serverPort)
        self.loginButton.clicked.connect(self.Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login, serverPort):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Login"))
        self.usr.setPlaceholderText(_translate("Login", "Your UserName"))
        self.pwd.setPlaceholderText(_translate("Login", "Your Password"))
        self.loginButton.setText(_translate("Login", "Login"))
        self.port.setText(_translate("Login", str(serverPort)))
        self.port.setPlaceholderText(_translate("Login", "Your ChatRoomID"))


    def Login(self):
        admin = [['linyijun', 'linyijun'], ['reneedress', 'reneedress']]
        username = str(self.usr.text())
        password = str(self.pwd.text())
        usrpwd = [username, password]
        if usrpwd in admin:
            # self.setResult(1)
            print('accept')
            # QtWidgets.QMessageBox.information(self.loginButton, "login", "login")
            # print('info done')
            self.accept()
            # self.close()
        else:
            self.reject()
            # self.setResult(0)

    def __init__(self, port):
        super(Ui_Login, self).__init__()
        self.setupUi(self, port)
        self.retranslateUi(self, port)
        self.show()

    # @QtCore.pyqtSlot()
    # def accept(self):
    #     pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    loginWindow = QDialog()
    ui = Ui_Login() # 这里的名字参考生成的py的类名
    ui.setupUi(loginWindow)
    loginWindow.show()
    sys.exit(app.exec_())