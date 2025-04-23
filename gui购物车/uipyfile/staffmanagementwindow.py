# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\python_project\PythonProject\jieduanyi\gui购物车\qtfile\staffmanagementwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_StaffManagementWindow(object):
    def setupUi(self, StaffManagementWindow):
        StaffManagementWindow.setObjectName("StaffManagementWindow")
        StaffManagementWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(StaffManagementWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.updatepushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("华文行楷")
        font.setPointSize(16)
        self.updatepushButton.setFont(font)
        self.updatepushButton.setObjectName("updatepushButton")
        self.gridLayout.addWidget(self.updatepushButton, 2, 0, 1, 1)
        self.deletepushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("华文行楷")
        font.setPointSize(16)
        self.deletepushButton.setFont(font)
        self.deletepushButton.setObjectName("deletepushButton")
        self.gridLayout.addWidget(self.deletepushButton, 1, 0, 1, 1)
        self.returnpushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("华文行楷")
        font.setPointSize(16)
        self.returnpushButton.setFont(font)
        self.returnpushButton.setObjectName("returnpushButton")
        self.gridLayout.addWidget(self.returnpushButton, 3, 0, 1, 1)
        self.addpushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("华文行楷")
        font.setPointSize(16)
        self.addpushButton.setFont(font)
        self.addpushButton.setObjectName("addpushButton")
        self.gridLayout.addWidget(self.addpushButton, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout_2.addWidget(self.tableWidget, 0, 0, 1, 1)
        StaffManagementWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(StaffManagementWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        StaffManagementWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(StaffManagementWindow)
        self.statusbar.setObjectName("statusbar")
        StaffManagementWindow.setStatusBar(self.statusbar)

        self.retranslateUi(StaffManagementWindow)
        QtCore.QMetaObject.connectSlotsByName(StaffManagementWindow)

    def retranslateUi(self, StaffManagementWindow):
        _translate = QtCore.QCoreApplication.translate
        StaffManagementWindow.setWindowTitle(_translate("StaffManagementWindow", "MainWindow"))
        self.updatepushButton.setText(_translate("StaffManagementWindow", "更新"))
        self.deletepushButton.setText(_translate("StaffManagementWindow", "删除"))
        self.returnpushButton.setText(_translate("StaffManagementWindow", "返回主界面"))
        self.addpushButton.setText(_translate("StaffManagementWindow", "增加"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StaffManagementWindow = QtWidgets.QMainWindow()
    ui = Ui_StaffManagementWindow()
    ui.setupUi(StaffManagementWindow)
    StaffManagementWindow.show()
    sys.exit(app.exec_())

