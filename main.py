from PyQt5 import QtCore, QtGui, QtWidgets
from pass_gen import Ui_MainWindow
import random

class PassGen(QtWidgets.QMainWindow):
    def __init__(self):
        super(PassGen, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.ui.generate.clicked.connect(self.password_generate)
        self.ui.closeApp.clicked.connect(self.close)
        self.show()



    def password_generate(self):
        password_len = self.get_pass_len()

        password = ''
        spec_symb ='/*&#$%()!@_=~|'
        numbers = '0123456789'
        small_symb = 'qwertyuiopasdfghjklzxcvbnm'
        big_symb = 'QWERTYUIOPASDFGHJKLZXCVBNM'
        symbols = ''


        if self.ui.specSym.isChecked() == True:
            symbols += spec_symb
        if self.ui.bigSym.isChecked() == True:
            symbols += big_symb
        if self.ui.smallSym.isChecked() == True:
            symbols += small_symb
        if self.ui.numbers.isChecked() == True:
            symbols += numbers


        try:
            for i in range(0, int(password_len)):
                try:
                    password += random.choice(symbols)
                except IndexError:
                    password = 'Choose parameters '
        except ValueError:
            password = 'Enter password lenght(int)'

        if password_len == '0':
            password = 'Password lenght cant be = 0'

        self.ui.result.setText(password)


    def get_pass_len(self):
        return str(self.ui.password_len.text())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    load = PassGen()
    sys.exit(app.exec_())