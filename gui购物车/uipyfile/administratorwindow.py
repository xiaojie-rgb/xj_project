# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\python_project\PythonProject\jieduanyi\gui购物车\qtfile\administratorwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AdministratorWindow(object):
    def setupUi(self, AdministratorWindow):
        AdministratorWindow.setObjectName("AdministratorWindow")
        AdministratorWindow.resize(1102, 702)
        self.centralwidget = QtWidgets.QWidget(AdministratorWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(260, 260, 501, 221))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.staffpushButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.staffpushButton.sizePolicy().hasHeightForWidth())
        self.staffpushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("华文行楷")
        font.setPointSize(16)
        self.staffpushButton.setFont(font)
        self.staffpushButton.setObjectName("staffpushButton")
        self.horizontalLayout.addWidget(self.staffpushButton)
        self.cargopushButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cargopushButton.sizePolicy().hasHeightForWidth())
        self.cargopushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("华文行楷")
        font.setPointSize(16)
        self.cargopushButton.setFont(font)
        self.cargopushButton.setObjectName("cargopushButton")
        self.horizontalLayout.addWidget(self.cargopushButton)
        AdministratorWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AdministratorWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1102, 26))
        self.menubar.setObjectName("menubar")
        AdministratorWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AdministratorWindow)
        self.statusbar.setObjectName("statusbar")
        AdministratorWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AdministratorWindow)
        QtCore.QMetaObject.connectSlotsByName(AdministratorWindow)

    def retranslateUi(self, AdministratorWindow):
        _translate = QtCore.QCoreApplication.translate
        AdministratorWindow.setWindowTitle(_translate("AdministratorWindow", "MainWindow"))
        self.staffpushButton.setText(_translate("AdministratorWindow", "员工管理"))
        self.cargopushButton.setText(_translate("AdministratorWindow", "货物管理"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AdministratorWindow = QtWidgets.QMainWindow()
    ui = Ui_AdministratorWindow()
    ui.setupUi(AdministratorWindow)
    AdministratorWindow.show()
    sys.exit(app.exec_())

