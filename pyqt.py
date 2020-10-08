import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
# 对应之前生成的py文件名
from gui import *
from login import *




if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    loginWindow = QDialog()
    ui = Ui_Login() # 这里的名字参考生成的py的类名
    ui.setupUi(loginWindow)
    ui_main = Ui_main()
    # loginWindow.show()
    print('loginWindow.')
    signal = loginWindow.exec_()
    if signal != QtWidgets.QDialog.Accepted:
        print('Accepted.')
        ui_main.setupUi(mainWindow)
        mainWindow.show()
    else:
        print('Rejected.')
    sys.exit(app.exec_())