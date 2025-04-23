from uipyfile.staffwindow import Ui_StaffWindow
from PyQt5.Qt import QApplication, QMainWindow,QMessageBox
from logic_code import shopping, staffmanagement,login


class StaffWindow(QMainWindow):
    def __init__(self,user_id,qxid):
        super().__init__()
        self.user_id = user_id
        self.qxid = qxid
        # 创建界面实例
        self.ui = Ui_StaffWindow()
        # 设置界面到窗口
        self.ui.setupUi(self)
        # 连接按钮的点击信号到对应的槽函数
        self.ui.shoppingButton.clicked.connect(self.handle_shopping_button_click)
        self.ui.inquireButton.clicked.connect(self.handle_inquire_button_click)
        self.ui.pushButton.clicked.connect(self.return_login)
        print(type(self.user_id))

    def handle_shopping_button_click(self):
        """处理购物按钮点击的槽函数"""
        try:
            self.close()

            self.shoppingwindow = shopping.ShoppingWindow(self.user_id,self.qxid)

            self.shoppingwindow.show()
        except Exception as e:
            print(e)
    def handle_inquire_button_click(self):
        '''处理后台查询按钮点击的槽函数'''
        print(2)
        try:
            if self.qxid == 1:
                print(3)
                self.close()
                try:
                    self.StaffManagementWindow = staffmanagement.StaffManagementWindow(self.user_id,self.qxid)
                    self.StaffManagementWindow.show()
                except Exception as e:
                    print(e)
            elif self.qxid == 0:
                print(1)
                QMessageBox.warning(self,'警告','普通用户不可进入此界面!')
        except Exception as e:
            print(e)

    def return_login(self):
        try:
            reply = QMessageBox.question(
                self,
                '退出确认',
                '是否退出登录',
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No
            )
            if reply == QMessageBox.Yes:
                self.close()
                self.loginwindow = login.LoginWindow()
                self.loginwindow.show()
            else:
                # 点击否执行的代码（可留空）
                pass
        except Exception as e:
            print(e)