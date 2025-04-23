import hashlib
import re
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from uipyfile.registrationwindow import Ui_RegistrationWindow
from logic_code import login
from mysql import connection
import pymysql

class RegisiterWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 创建界面实例
        self.ui = Ui_RegistrationWindow()
        # 设置界面到窗口
        self.ui.setupUi(self)
        # 连接注册按钮的点击事件到注册的函数
        self.ui.registrationButton.clicked.connect(self.register)

    def register(self):
        name = self.ui.namelineEdit.text()
        username = self.ui.usernamelineEdit.text()
        password = self.ui.passwordlineEdit.text()
        hashpassword = hashlib.md5(password.encode('utf-8')).hexdigest()
        pattern = re.compile(r'^[\u4e00-\u9fa5]{2,}$')  # 匹配至少2个及以上的中文字符
        if not pattern.fullmatch(name):
            QMessageBox.warning(self, '警告', '请输入合法姓名!')
            return

        for char in username:
            if not (char.isalpha() or char.isdigit() or char == '_'):
                QMessageBox.information(self, '提示', '用户名只能由数字、字母和下划线组成!')
                return
        if len(password) > 8:
            QMessageBox.information(self, '提示', '密码位数不能大于8位!')
            return
        else:
            for char in password:
                if not (char.isalpha() or char.isdigit()):
                    QMessageBox.information(self, '提示', '密码只能由数字和字母组成!')
                    return

        conn = connection()
        if conn:
            try:
                cursor = conn.cursor()
                create_table_query = """
                CREATE TABLE IF NOT EXISTS users (
                    ID INT PRIMARY KEY,
                    name VARCHAR(50) NOT NULL,
                    username VARCHAR(255) NOT NULL UNIQUE,
                    password VARCHAR(255) NOT NULL
                )
                """
                cursor.execute(create_table_query)

                if username and hashpassword:
                    try:
                        insert_user = 'INSERT INTO users (NAME, username, password,qxid) VALUES (%s, %s, %s,%s)'
                        cursor.execute(insert_user, (name, username, hashpassword,0))
                        conn.commit()
                        print(1)
                        QMessageBox.information(self,"注册成功", "用户注册成功！")
                        self.close()
                        self.login = login.LoginWindow()
                        self.login.show()
                    except pymysql.IntegrityError:
                        QMessageBox.critical(self, "注册失败", "用户名已存在，请选择其他用户名。")
                else:
                    QMessageBox.critical(self, "注册失败", "请输入用户名和密码。")
            except pymysql.Error as e:
                QMessageBox.critical(self, '错误', f'数据库操作出错: {e}')
            finally:
                conn.close()