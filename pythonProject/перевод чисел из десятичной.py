import sys
import math

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.dis = ''
        self.dis2 = ''
        uic.loadUi('calc.ui', self)
        self.btn0.clicked.connect(self.ret0)
        self.btn1.clicked.connect(self.ret1)
        self.btn2.clicked.connect(self.ret2)
        self.btn3.clicked.connect(self.ret3)
        self.btn4.clicked.connect(self.ret4)
        self.btn5.clicked.connect(self.ret5)
        self.btn6.clicked.connect(self.ret6)
        self.btn7.clicked.connect(self.ret7)
        self.btn8.clicked.connect(self.ret8)
        self.btn9.clicked.connect(self.ret9)
        self.btn_clear.clicked.connect(self.cleardis)
        self.btn_div.clicked.connect(self.div)
        self.btn_dot.clicked.connect(self.dot)
        self.btn_eq.clicked.connect(self.eq)
        self.btn_fact.clicked.connect(self.fact)
        self.btn_minus.clicked.connect(self.minus)
        self.btn_mult.clicked.connect(self.mult)
        self.btn_plus.clicked.connect(self.plus)
        self.btn_pow.clicked.connect(self.pow)
        self.btn_sqrt.clicked.connect(self.sqrt)

    def ret0(self):
        self.dis += '0'
        self.dis2 += '0'
        self.table.display(self.dis2)

    def ret1(self):
        self.dis += '1'
        self.dis2 += '1'
        self.table.display(self.dis2)

    def ret2(self):
        self.dis += '2'
        self.dis2 += '2'
        self.table.display(self.dis2)

    def ret3(self):
        self.dis += '3'
        self.dis2 += '3'
        self.table.display(self.dis2)

    def ret4(self):
        self.dis += '4'
        self.dis2 += '4'
        self.table.display(self.dis2)

    def ret5(self):
        self.dis += '5'
        self.dis2 += '5'
        self.table.display(self.dis2)

    def ret6(self):
        self.dis += '6'
        self.dis2 += '6'
        self.table.display(self.dis2)

    def ret7(self):
        self.dis += '7'
        self.dis2 += '7'
        self.table.display(self.dis2)

    def ret8(self):
        self.dis += '8'
        self.dis2 += '8'
        self.table.display(self.dis2)

    def ret9(self):
        self.dis += '9'
        self.dis2 += '9'
        self.table.display(self.dis2)

    def cleardis(self):
        self.dis = ''
        self.dis2 = ''
        self.table.display('')

    def div(self):
        self.dis += '/ '
        self.dis2 = ''

    def dot(self):
        self.dis += '.'
        self.dis2 += '.'
        self.table.display(self.dis2)

    def eq(self):
        if '/0' not in self.dis:
            a = eval(self.dis)
            self.table.display(a)
        else:
            self.table.display('Error')

    def fact(self):
        if ' ' in self.dis:
            self.dis = self.dis.split(' ')
            fac = math.factorial(int(self.dis[-1]))
            self.dis[-1] = str(fac)
            self.dis = ''.join(self.dis)
        else:
            self.dis = str(math.factorial(int(self.dis)))

    def minus(self):
        self.dis += '- '
        self.dis2 = ''

    def mult(self):
        self.dis += '* '
        self.dis2 = ''

    def plus(self):
        self.dis += '+ '
        self.dis2 = ''

    def pow(self):
        self.dis += '** '
        self.dis2 = ''

    def sqrt(self):
        self.dis += '**0.5 '
        self.dis2 = ''


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculator()
    ex.show()
    sys.exit(app.exec_())
