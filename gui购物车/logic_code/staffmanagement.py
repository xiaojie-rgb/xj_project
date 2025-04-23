from PyQt5.Qt import QMainWindow, QMessageBox
from PyQt5.QtWidgets import QTableWidgetItem, QAbstractItemView
from logic_code import staff
from logic_code import cargo
from uipyfile.staffmanagementwindow import Ui_StaffManagementWindow
from mysql import connection
import pymysql
class StaffManagementWindow(QMainWindow):
    def __init__(self,user_id,qxid):
        super().__init__()
        self.user_id = user_id
        self.qxid = qxid
        # 创建界面实例
        self.ui = Ui_StaffManagementWindow()
        # 设置界面到窗口
        self.ui.setupUi(self)
        # 获取正在销售的表格
        self.table = self.ui.tableWidget
        # 获取正在销售的表格控件
        self.ui.addpushButton.clicked.connect(self.addAll)  # 添加按钮
        self.ui.deletepushButton.clicked.connect(self.delete)  # 删除按钮
        self.ui.updatepushButton.clicked.connect(self.update)  # 更新按钮
        self.ui.returnpushButton.clicked.connect(self.returnstaff)  # 返回主界面按钮
        self.filltab() #展示界面

    def filltab(self):
        conn = connection()
        if conn:
            try:
                cursor = conn.cursor()
                query = "SELECT name,price,num FROM shop WHERE state = %s"
                cursor.execute(query,(1,))
                result = cursor.fetchall()
                # 设置表格控件的行数为商品数据列表的长度
                self.table.setRowCount(len(result))
                # 设置表格控件的列数为商品数据列表中第一个元素的长度
                self.table.setColumnCount(len(result[0]))
                # 设置表头
                headers = ['商品名称', '商品价格','数量']
                self.table.setHorizontalHeaderLabels(headers)

                # 添加表格数据
                for row, row_data in enumerate(result):
                    for col, item_txt in enumerate(row_data):
                        item = str(item_txt)
                        self.table.setItem(row, col, QTableWidgetItem(item))
                #  完全禁用QTableView的单元格编辑功能,使用户无法进行编辑
                self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
            except pymysql.Error as e:
                QMessageBox.warning(self, '警告', f'数据库操作错误:{e}')
                print(e)
            finally:
                conn.close()
    def addAll(self):
        try:
            self.close()
            self.cargowindow = cargo.CargoWindow(self.user_id,self.qxid,1)
            self.cargowindow.show()
        except Exception as e:
            print(e)
    def delete(self):
        try:
            conn = connection()
            if conn:
                try:
                    select_item = self.table.selectedItems()

                    # 得到选中的值
                    row = select_item[0].row()
                    wor = self.table.item(row, 0).text()

                    # 从数据库中跟新state的值为0,表示从购物车中删除
                    cursor = conn.cursor()
                    query = 'UPDATE shop SET state = 0 WHERE NAME = %s'
                    cursor.execute(query, wor)
                    conn.commit()
                    # 从显示的表中删除
                    self.table.removeRow(select_item[0].row())
                except pymysql.Error as e:
                    QMessageBox.warning(self, '警告', f'数据库操作有误{e}')
                finally:
                    conn.close()
        except Exception as e:
            QMessageBox.warning(self, '警告', '请选择正确的区域!')
            print(e)
    def returnstaff(self):
        try:
            self.close()
            self.staffwindow = staff.StaffWindow(self.user_id,self.qxid)
            self.staffwindow.show()
        except Exception as e:
            print(e)
    def update(self):
        # QMessageBox.information(self, '提示', '更新完毕!')
        self.close()
        self.cargowindow = cargo.CargoWindow(self.user_id,self.qxid,2)
        self.cargowindow.show()