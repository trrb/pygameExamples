import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, \
    QLabel


class Evaluator(QWidget):
    def __init__(self):
        super().__init__()
        self.second_value = None
        self.first_value = None
        self.trick_button = None
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 325, 100)
        self.setWindowTitle('Evaluator')
        self.trick_button = QPushButton('->', self)
        self.trick_button.resize(40, 40)
        self.trick_button.move(125, 30)
        self.trick_button.clicked.connect(self.trick_but)
        self.first_value = QLineEdit(self)
        self.first_value.move(20, 30)
        self.first_value.resize(100, 40)
        self.second_value = QLineEdit(self)
        self.second_value.move(170, 30)
        self.second_value.resize(100, 40)
        self.expression = QLabel('Выражение:', self)
        self.expression.move(20, 10)
        self.result = QLabel('Результат:', self)
        self.result.move(170, 10)

    def trick_but(self):
        self.second_value.setText(str(eval(self.first_value.text())))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    word = Evaluator()
    word.show()
    sys.exit(app.exec())
