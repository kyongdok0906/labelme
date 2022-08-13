import sys

from qtpy import QtWidgets, QtCore


class LoginDLG(QtWidgets.QWidget):

    def __init__(self):
        # self.mainwin = appOBJ
        super().__init__()
        self.initUI()

    def initUI(self):
       # self.mainwin.hide()
       # self.mainwin.raise_()
        grid = QtWidgets.QGridLayout()
        grid.setContentsMargins(20, 20, 20, 10)
        grid.setVerticalSpacing(10)
        self.setLayout(grid)

        lb_uname = QtWidgets.QLabel('UserName *')
        grid.addWidget(lb_uname, 0, 0, QtCore.Qt.AlignLeft)
        lb_uname_edit = QtWidgets.QLineEdit()
        lb_uname_edit.setFixedWidth(150)
        grid.addWidget(lb_uname_edit, 0, 1, QtCore.Qt.AlignLeft)

        lb_pwd = QtWidgets.QLabel('Password *')
        grid.addWidget(lb_pwd, 1, 0, QtCore.Qt.AlignLeft)
        lb_pwd_edit = QtWidgets.QLineEdit()
        lb_pwd_edit.setFixedWidth(150)
        grid.addWidget(lb_pwd_edit, 1, 1, QtCore.Qt.AlignLeft)

        lb_lang = QtWidgets.QLabel('Language ')
        grid.addWidget(lb_lang, 2, 0, QtCore.Qt.AlignLeft)

        cb = QtWidgets.QComboBox()
        cb.addItem('English')
        cb.addItem('Korean')
        cb.addItem('Chinese')
        cb.setFixedWidth(100)
        # cb.activated[str].connect(self.onActivated)
        grid.addWidget(cb, 2, 1, QtCore.Qt.AlignLeft)

        btn_login = QtWidgets.QPushButton('Login')
        btn_login.setFixedWidth(100)
        btn_login.clicked.connect(self.loginAction)
        grid.addWidget(btn_login, 3, 1, QtCore.Qt.AlignLeft)

        lb_alram = QtWidgets.QLabel('...')
        lb_alram.setFixedWidth(200)
        grid.addWidget(lb_alram, 4, 1, QtCore.Qt.AlignLeft)

        self.setWindowTitle('Login Form')
        self.setGeometry(300, 300, 200, 150)
        # position = QtCore.QPoint(0, 0)
        # self.move(position)

    def loginAction(self):
        print("click login btn")
        return

