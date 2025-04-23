import pymysql
from PyQt5.Qt import QMainWindow
from PyQt5.QtWidgets import QMessageBox

from mysql import connection
from uipyfile.cargowindow import Ui_CargoWindow
from logic_code import staffmanagement


class CargoWindow(QMainWindow):

    def __init__(self, user_id,qxid,state):
        super().__init__()
        self.user_id = user_id
        self.qxid=qxid
        self.state = state
        # 创建界面实例
        self.ui = Ui_CargoWindow()
        # 设置界面到窗口
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.add)
        self.ui.returnButton.clicked.connect(self.ret)


    # 返回按钮
    def ret(self):
        self.close()
        self.staffmanagementwindow = staffmanagement.StaffManagementWindow(self.user_id,self.qxid)
        self.staffmanagementwindow.show()

    def add(self):
        if self.state == 1:
            name = self.ui.productNameEdit.text()
            price = self.ui.priceLineEdit.text()
            num = self.ui.amountLineEdit.text()
            conn = connection()
            if conn:
                try:
                    # 添加到数据库
                    cursor = conn.cursor()
                    query = "SELECT name FROM shop WHERE name = %s AND state = %s"
                    cursor.execute(query, (name, 1))
                    result = cursor.fetchall()
                    # print(result)
                    # 如果有同名商品
                    if result:
                        QMessageBox.information(self, '提示', '已有同名商品!')
                        # self.close()
                        # self.staffmanagementwindow = staffmanagement.StaffManagementWindow(self.user_id)
                        # self.staffmanagementwindow.show()

                    # 如果没有同名商品
                    else:
                        query = "INSERT INTO SHOP(name, price,num,state) VALUES (%s, %s,%s,%s)"
                        cursor.execute(query, (name, price, num, 1))
                        conn.commit()
                        QMessageBox.information(self, '提示', f'已加入新商品{name}')

                except pymysql.Error as e:
                    QMessageBox.critical(self, '错误', f'数据库操作出错: {e}')
                finally:
                    conn.close()
        try:
            if self.state == 2:
                name = self.ui.productNameEdit.text()
                price = self.ui.priceLineEdit.text()
                num = self.ui.amountLineEdit.text()
                conn = connection()
                if conn:
                    try:
                        # 添加到数据库
                        cursor = conn.cursor()
                        query = "SELECT name FROM shop WHERE name = %s AND state = %s"
                        cursor.execute(query, (name, 1))
                        result = cursor.fetchall()
                        # print(result)
                        # 如果有同名商品
                        if result:
                            query = "UPDATE SHOP SET price = %s, num = %s WHERE name = %s"
                            cursor.execute(query, (price, num, name))
                            conn.commit()
                            QMessageBox.information(self,'提示', f'已更新{name}的价格为{price},数量为{num}')
                            # self.close()
                            # self.staffmanagementwindow = staffmanagement.StaffManagementWindow(self.user_id)
                            # self.staffmanagementwindow.show()

                        # 如果没有同名商品
                        else:
                            QMessageBox.information(self,'提示', '没有该商品,不可进行更新!')

                    except pymysql.Error as e:
                        QMessageBox.critical(self, '错误', f'数据库操作出错: {e}')
                    finally:
                        conn.close()
        except Exception as e:
            print(e)