from PyQt5.QtWidgets import QMainWindow, QMessageBox
from uipyfile.administratorwindow import Ui_AdministratorWindow
from logic_code import register,staff
from mysql import connection
import pymysql

class AdministratorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 创建界面实例
        self.ui = Ui_AdministratorWindow()
        # 设置界面到窗口
        self.ui.setupUi(self)
        # 连接员工管理按钮的点击事件到员工管理的函数
        self.ui.staffpushButton.clicked.connect(self.yuangong)
        # 连接货物管理按钮的点击事件到货物管理的函数
        self.ui.cargopushButton.clicked.connect(self.huowu)

    def yuangong(self):
        pass
    def huowu(self):
        pass
