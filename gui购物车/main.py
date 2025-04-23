import sys
from logic_code import login
from PyQt5.Qt import QApplication


if __name__ == '__main__':
    app = QApplication(sys.argv)
    try:
        window = login.LoginWindow()
        window.show()
    except Exception as e:
        print(e)
    sys.exit(app.exec_())