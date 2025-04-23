from PyQt5.QtWidgets import QTableWidgetItem, QAbstractItemView

import pymysql

from uipyfile.shoppingwindow import Ui_ShoppingWindow
from PyQt5.Qt import QMainWindow, QMessageBox
from logic_code import staff
from mysql import connection
from logic_code import login


class ShoppingWindow(QMainWindow):
    def __init__(self, user_id,qxid):
        super().__init__()
        # 创建界面实例
        self.ui = Ui_ShoppingWindow()
        self.qxid = qxid
        # 设置界面到窗口
        self.ui.setupUi(self)
        # 连接按钮的点击信号到对应的槽函数
        self.ui.selectButton.clicked.connect(self.add_car)  # 选择按钮
        #  获取'正在销售'表格
        self.sale_table = self.ui.salesTableWidget
        #  获取'购物车'表格
        self.history_table = self.ui.historyTableWidget
        # 获取售卖表格控件
        self.ui.updateButton.clicked.connect(self.update)  # 删除按钮
        self.ui.returnButton.clicked.connect(self.returnButtonClicked)  # 返回按钮
        self.ui.settlementButton.clicked.connect(self.settlementButtonClicked)  # 结算按钮
        #  销售数据内容函数
        self.filltab()
        self.id = user_id
        self.fillcartab()
        # self.id = user_id

    def filltab(self):
        conn = connection()
        if conn:
            try:
                cursor = conn.cursor()
                query = "SELECT name,price FROM shop where state=%s"
                cursor.execute(query, (1,))
                result = cursor.fetchall()
                # 设置表格控件的行数为商品数据列表的长度
                self.sale_table.setRowCount(len(result))
                # 设置表格控件的列数为商品数据列表中第一个元素的长度
                self.sale_table.setColumnCount(len(result[0]))
                # 设置表头
                headers = ['商品名称', '商品价格']
                self.sale_table.setHorizontalHeaderLabels(headers)

                # 添加表格数据
                for row, row_data in enumerate(result):
                    for col, item_txt in enumerate(row_data):
                        item = str(item_txt)
                        self.sale_table.setItem(row, col, QTableWidgetItem(item))
                #  完全禁用QTableView的单元格编辑功能,使用户无法进行编辑
                self.sale_table.setEditTriggers(QAbstractItemView.NoEditTriggers)


            except pymysql.Error as e:
                QMessageBox.warning(self, '警告', f'数据库操作错误:{e}')
                print(e)
            finally:
                conn.close()

    def fillcartab(self):
        conn = connection()
        if conn:
            try:
                cursor = conn.cursor()
                try:
                    query = ("SELECT name,price,num,numprice FROM CAR WHERE id = %s AND state = %s AND settlement = %s")
                    cursor.execute(query, (self.id, 1, 1))
                    result = cursor.fetchall()
                except pymysql.Error as e:
                    print(e)
                headers = ['商品名称', '商品价格', '商品数量', '总价']
                # 设置表格控件的行数为商品数据列表的长度
                self.history_table.setRowCount(len(result))
                # 检查 result 是否为空
                if result:
                    # 设置表格控件的列数为商品数据列表第一个元素的长度
                    self.history_table.setColumnCount(len(result[0]))
                else:
                    # 如果 result 为空，将列数设为 0
                    self.history_table.setColumnCount(0)

                self.history_table.setHorizontalHeaderLabels(headers)

                # 循环把数据库中的内容添加到表格中
                for row, row_data in enumerate(result):
                    for col, item_txt in enumerate(row_data):
                        item = str(item_txt)
                        self.history_table.setItem(row, col, QTableWidgetItem(item))
                #  完全禁用QTableView的单元格编辑功能,使用户无法进行编辑
                self.history_table.setEditTriggers(QAbstractItemView.NoEditTriggers)

            except pymysql.Error as e:
                QMessageBox.warning(self, '警告', f'数据库操作错误{e}')
            finally:
                conn.close()

    def add_car(self):
        select_item = self.sale_table.selectedItems()  # 获取选中的内容
        conn = connection()
        if conn:
            try:
                if select_item:
                    #  数量
                    quantity = self.ui.amountLineEdit.text()
                    if quantity == '':
                        quantity = 1
                    cursor = conn.cursor()
                    # 获取选中行的商品名称和价格
                    row = select_item[0].row()
                    name = self.sale_table.item(row, 0).text()  # 假设第一列是商品名称
                    price = self.sale_table.item(row, 1).text()  # 假设第二列是商品价格
                    numprice = int(price) * int(quantity)
                    # 添加商品
                    query = "SELECT * FROM CAR WHERE name = %s AND state = %s AND ID =%s AND settlement = %s"
                    cursor.execute(query, (name, 1, self.id, 1))
                    result = cursor.fetchall()
                    # print(result)
                    if result:
                        query = "UPDATE CAR SET num = %s,numprice = %s WHERE name = %s"
                        cursor.execute(query, (result[0][2] + int(quantity), result[0][3] + numprice, name))
                        conn.commit()
                    else:
                        # 插入完整的商品记录
                        query = "INSERT INTO CAR(name, price, NUM,NUMPRICE,ID,STATE,settlement) VALUES (%s, %s, %s,%s,%s,%s,%s)"
                        cursor.execute(query, (name, price, quantity, numprice, self.id, 1, 1))
                        conn.commit()
                        # 调用展示表格数据的函数
                    self.fillcartab()
            except Exception as e:
                print(e)
                # QMessageBox.warning(self,'警告', '{e}')
            finally:
                conn.close()

    # 删除按钮的槽函数
    def update(self):
        try:
            conn = connection()
            if conn:
                try:
                    select_item = self.history_table.selectedItems()

                    # 得到选中的值
                    row = select_item[0].row()
                    wor = self.history_table.item(row, 0).text()

                    # 从数据库中跟新state的值为0,表示从购物车中删除
                    cursor = conn.cursor()
                    query = 'UPDATE CAR SET state = 0 WHERE NAME = %s'
                    cursor.execute(query, wor)
                    conn.commit()
                    # 从显示的表中删除
                    self.history_table.removeRow(select_item[0].row())
                except pymysql.Error as e:
                    QMessageBox.warning(self, '警告', f'数据库操作有误{e}')
                finally:
                    conn.close()
        except Exception as e:
            QMessageBox.warning(self, '警告', '请选择正确的区域!')
            print(e)

    def returnButtonClicked(self):
        try:
            self.close()
            self.staffwindow = staff.StaffWindow(self.id,self.qxid)
            self.staffwindow.show()
        except Exception as e:
            print(e)

    def settlementButtonClicked(self):
        select_item = self.history_table.selectedItems()  # 获取选中的内容
        # print(select_item)
        if select_item:
            row = select_item[0].row()
            # print(row)
            name = self.history_table.item(row, 0).text()  # 假设第一列是商品名称
            numprice = self.history_table.item(row, 3).text()
            # print(name)
            # 从数据库中跟新settlement的值为0,表示已经从购物车结算
            try:
                conn = connection()
                cursor = conn.cursor()
                query = 'UPDATE CAR SET settlement = 0 WHERE NAME = %s'
                cursor.execute(query, (name))
                conn.commit()
                QMessageBox.information(self, '提示', f'正在结算,价格为{numprice}')
                # 调用展示表格数据的函数
                self.fillcartab()
            except Exception as e:
                print(e)
        else:
            reply = QMessageBox.question(
                self,
                '结算确认',
                '是否结算全部商品',
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No
            )
            try:
                if reply == QMessageBox.Yes:
                    # 点击确定后执行的代码
                    conn = connection()
                    cursor = conn.cursor()
                    query = 'select numprice from CAR where id = %s AND settlement = %s AND state = %s'
                    cursor.execute(query, (self.id, 1, 1))
                    result = cursor.fetchall()
                    # print(result)
                    num = 0
                    for i in result:
                        for j in i:
                            num += j
                    print(num)
                    conn.commit()
                    query = 'UPDATE CAR SET settlement = 0 where id = %s AND state = %s'
                    cursor.execute(query, (self.id, 1))
                    conn.commit()
                    QMessageBox.information(self, '提示', f'正在结算,价格为{num}')
                    self.fillcartab()
                else:
                    # 点击否执行的代码（可留空）
                    pass
            except Exception as e:
                print(e)
