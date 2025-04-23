import hashlib

from PyQt5.QtWidgets import QMainWindow, QMessageBox
from uipyfile.loginwindow import Ui_LoginWindow
from logic_code import register, staff, administrator
from mysql import connection
import pymysql


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 创建界面实例
        self.ui = Ui_LoginWindow()
        # 设置界面到窗口
        self.ui.setupUi(self)
        # 连接登录按钮的点击事件到登录的函数
        self.ui.pushButton.clicked.connect(self.login)

        # self.id = None

    def login(self):
        username = self.ui.usernamelineEdit.text()
        password = self.ui.passwordlineEdit.text()
        hashpassword = hashlib.md5(password.encode('utf-8')).hexdigest()
        conn = connection()
        if conn:
            try:
                cursor = conn.cursor()

                query = "SELECT name FROM users WHERE username = %s"
                # print(query)
                cursor.execute(query, (username,))
                result = cursor.fetchone()
                # print(result)
                if result is None:
                    QMessageBox.critical(self, '错误', '无此账号,请进行注册!')
                    try:
                        # print(1)
                        self.close()
                        # print(2)
                        self.regisiterwindow = register.RegisiterWindow()
                        # print(3)
                        self.regisiterwindow.show()
                    except Exception as e:
                        print(e)
                else:
                    query = "SELECT * FROM users WHERE username = %s"
                    cursor.execute(query, (username,))
                    result = cursor.fetchone()
                    # print(result)
                    if result[4] == 1:
                        QMessageBox.information(self, '提示', '欢迎管理员登录!')
                        # self.close()
                        try:
                            query = "SELECT ID,qxid FROM users WHERE username = %s AND password = %s"
                            print(query)
                            cursor.execute(query, (username, hashpassword))
                            result = cursor.fetchone()  # 接收到的是一个元组,例如(3,)
                            # print(result)
                            self.id = result[0]
                            self.qxid = result[1]
                            self.staffwindow = staff.StaffWindow(self.id,self.qxid)
                            self.close()
                            self.staffwindow.show()
                        except Exception as e:
                            print(e)
                    elif result[4] == 0:
                        if result[3] == hashpassword:
                            QMessageBox.information(self, '提示', '登陆成功')
                            query = "SELECT ID,qxid FROM users WHERE username = %s AND password = %s"
                            cursor.execute(query, (username, hashpassword))
                            result = cursor.fetchone()  # 接收到的是一个元组,例如(3,)
                            # print(result)
                            self.id = result[0]
                            self.qxid = result[1]
                            # print(self.id)
                            self.close()
                            self.staffwindow = staff.StaffWindow(self.id,self.qxid)
                            self.staffwindow.show()
                        else:
                            QMessageBox.warning(self, '警告', '密码错误!请重试!')
            except pymysql.Error as e:
                QMessageBox.critical(self, '错误', f'数据库操作出错: {e}')
            finally:
                conn.close()
