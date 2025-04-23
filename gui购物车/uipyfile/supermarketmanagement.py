# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\python_project\PythonProject\jieduanyi\gui购物车\qtfile\supermarketmanagement.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SupermarketManagement(object):
    def setupUi(self, SupermarketManagement):
        SupermarketManagement.setObjectName("SupermarketManagement")
        SupermarketManagement.resize(1118, 770)
        self.centralWidget = QtWidgets.QWidget(SupermarketManagement)
        self.centralWidget.setObjectName("centralWidget")
        self.advertisingLabel = QtWidgets.QLabel(self.centralWidget)
        self.advertisingLabel.setGeometry(QtCore.QRect(384, 270, 281, 41))
        font = QtGui.QFont()
        font.setFamily("华文行楷")
        font.setPointSize(16)
        self.advertisingLabel.setFont(font)
        self.advertisingLabel.setObjectName("advertisingLabel")
        self.advertisingLabel_2 = QtWidgets.QLabel(self.centralWidget)
        self.advertisingLabel_2.setGeometry(QtCore.QRect(384, 330, 281, 41))
        font = QtGui.QFont()
        font.setFamily("华文行楷")
        font.setPointSize(16)
        self.advertisingLabel_2.setFont(font)
        self.advertisingLabel_2.setObjectName("advertisingLabel_2")
        SupermarketManagement.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(SupermarketManagement)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1118, 26))
        self.menuBar.setObjectName("menuBar")
        SupermarketManagement.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(SupermarketManagement)
        self.mainToolBar.setObjectName("mainToolBar")
        SupermarketManagement.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(SupermarketManagement)
        self.statusBar.setObjectName("statusBar")
        SupermarketManagement.setStatusBar(self.statusBar)

        self.retranslateUi(SupermarketManagement)
        QtCore.QMetaObject.connectSlotsByName(SupermarketManagement)

    def retranslateUi(self, SupermarketManagement):
        _translate = QtCore.QCoreApplication.translate
        SupermarketManagement.setWindowTitle(_translate("SupermarketManagement", "SupermarketManagement"))
        self.advertisingLabel.setText(_translate("SupermarketManagement", "广告招租 "))
        self.advertisingLabel_2.setText(_translate("SupermarketManagement", "联系方式：123465789"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SupermarketManagement = QtWidgets.QMainWindow()
    ui = Ui_SupermarketManagement()
    ui.setupUi(SupermarketManagement)
    SupermarketManagement.show()
    sys.exit(app.exec_())

