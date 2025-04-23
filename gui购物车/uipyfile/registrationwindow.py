# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\python_project\PythonProject\jieduanyi\gui购物车\qtfile\registrationwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RegistrationWindow(object):
    def setupUi(self, RegistrationWindow):
        RegistrationWindow.setObjectName("RegistrationWindow")
        RegistrationWindow.resize(1144, 803)
        self.centralwidget = QtWidgets.QWidget(RegistrationWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(294, 439, 459, 54))
        font = QtGui.QFont()
        font.setFamily("华文行楷")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(290, 190, 461, 251))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("华文行楷")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.namelineEdit = QtWidgets.QLineEdit(self.widget)
        self.namelineEdit.setObjectName("namelineEdit")
        self.gridLayout.addWidget(self.namelineEdit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("华文行楷")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.usernamelineEdit = QtWidgets.QLineEdit(self.widget)
        self.usernamelineEdit.setObjectName("usernamelineEdit")
        self.gridLayout.addWidget(self.usernamelineEdit, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
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
        self.passwordlineEdit = QtWidgets.QLineEdit(self.widget)
        self.passwordlineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordlineEdit.setObjectName("passwordlineEdit")
        self.gridLayout.addWidget(self.passwordlineEdit, 2, 1, 1, 1)
        self.registrationButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("华文行楷")
        font.setPointSize(16)
        self.registrationButton.setFont(font)
        self.registrationButton.setObjectName("registrationButton")
        self.gridLayout.addWidget(self.registrationButton, 3, 0, 1, 2)
        RegistrationWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(RegistrationWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1144, 26))
        self.menubar.setObjectName("menubar")
        RegistrationWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(RegistrationWindow)
        self.statusbar.setObjectName("statusbar")
        RegistrationWindow.setStatusBar(self.statusbar)

        self.retranslateUi(RegistrationWindow)
        QtCore.QMetaObject.connectSlotsByName(RegistrationWindow)

    def retranslateUi(self, RegistrationWindow):
        _translate = QtCore.QCoreApplication.translate
        RegistrationWindow.setWindowTitle(_translate("RegistrationWindow", "MainWindow"))
        self.label.setText(_translate("RegistrationWindow", "姓    名："))
        self.label_2.setText(_translate("RegistrationWindow", "用户名："))
        self.label_3.setText(_translate("RegistrationWindow", "密    码："))
        self.registrationButton.setText(_translate("RegistrationWindow", "注册"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RegistrationWindow = QtWidgets.QMainWindow()
    ui = Ui_RegistrationWindow()
    ui.setupUi(RegistrationWindow)
    RegistrationWindow.show()
    sys.exit(app.exec_())

