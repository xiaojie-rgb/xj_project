# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'staffwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_StaffWindow(object):
    def setupUi(self, StaffWindow):
        StaffWindow.setObjectName("StaffWindow")
        StaffWindow.resize(1119, 756)
        self.centralwidget = QtWidgets.QWidget(StaffWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(270, 250, 501, 221))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.shoppingButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shoppingButton.sizePolicy().hasHeightForWidth())
        self.shoppingButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("华文行楷")
        font.setPointSize(16)
        self.shoppingButton.setFont(font)
        self.shoppingButton.setObjectName("shoppingButton")
        self.horizontalLayout.addWidget(self.shoppingButton)
        self.inquireButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inquireButton.sizePolicy().hasHeightForWidth())
        self.inquireButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("华文行楷")
        font.setPointSize(16)
        self.inquireButton.setFont(font)
        self.inquireButton.setObjectName("inquireButton")
        self.horizontalLayout.addWidget(self.inquireButton)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(650, 500, 101, 41))
        font = QtGui.QFont()
        font.setFamily("华文行楷")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        StaffWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(StaffWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1119, 25))
        self.menubar.setObjectName("menubar")
        StaffWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(StaffWindow)
        self.statusbar.setObjectName("statusbar")
        StaffWindow.setStatusBar(self.statusbar)

        self.retranslateUi(StaffWindow)
        QtCore.QMetaObject.connectSlotsByName(StaffWindow)

    def retranslateUi(self, StaffWindow):
        _translate = QtCore.QCoreApplication.translate
        StaffWindow.setWindowTitle(_translate("StaffWindow", "MainWindow"))
        self.shoppingButton.setText(_translate("StaffWindow", "购物"))
        self.inquireButton.setText(_translate("StaffWindow", "后台管理"))
        self.pushButton.setText(_translate("StaffWindow", "退出登录"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StaffWindow = QtWidgets.QMainWindow()
    ui = Ui_StaffWindow()
    ui.setupUi(StaffWindow)
    StaffWindow.show()
    sys.exit(app.exec_())

