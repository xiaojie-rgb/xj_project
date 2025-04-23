# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\code\Spt2411\一阶段\gui购物车\qtfile\cargowindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CargoWindow(object):
    def setupUi(self, CargoWindow):
        CargoWindow.setObjectName("CargoWindow")
        CargoWindow.resize(1040, 714)
        self.centralwidget = QtWidgets.QWidget(CargoWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(300, 180, 451, 231))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("华文行楷")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.priceLineEdit = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.priceLineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.priceLineEdit.setObjectName("priceLineEdit")
        self.gridLayout.addWidget(self.priceLineEdit, 2, 1, 1, 1)
        self.productNameEdit = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.productNameEdit.setObjectName("productNameEdit")
        self.gridLayout.addWidget(self.productNameEdit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("华文行楷")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.amountLineEdit = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.amountLineEdit.setObjectName("amountLineEdit")
        self.gridLayout.addWidget(self.amountLineEdit, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("华文行楷")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(300, 410, 221, 38))
        font = QtGui.QFont()
        font.setFamily("华文行楷")
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.returnButton = QtWidgets.QPushButton(self.centralwidget)
        self.returnButton.setGeometry(QtCore.QRect(530, 410, 221, 38))
        font = QtGui.QFont()
        font.setFamily("华文行楷")
        font.setPointSize(16)
        self.returnButton.setFont(font)
        self.returnButton.setObjectName("returnButton")
        CargoWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CargoWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1040, 26))
        self.menubar.setObjectName("menubar")
        CargoWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CargoWindow)
        self.statusbar.setObjectName("statusbar")
        CargoWindow.setStatusBar(self.statusbar)

        self.retranslateUi(CargoWindow)
        QtCore.QMetaObject.connectSlotsByName(CargoWindow)

    def retranslateUi(self, CargoWindow):
        _translate = QtCore.QCoreApplication.translate
        CargoWindow.setWindowTitle(_translate("CargoWindow", "MainWindow"))
        self.label.setText(_translate("CargoWindow", "商品名："))
        self.label_2.setText(_translate("CargoWindow", "数    量："))
        self.label_3.setText(_translate("CargoWindow", "价    格："))
        self.pushButton.setText(_translate("CargoWindow", "确认"))
        self.returnButton.setText(_translate("CargoWindow", "返回"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CargoWindow = QtWidgets.QMainWindow()
    ui = Ui_CargoWindow()
    ui.setupUi(CargoWindow)
    CargoWindow.show()
    sys.exit(app.exec_())

