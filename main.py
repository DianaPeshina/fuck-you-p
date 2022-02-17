import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi

from calculate import isMatch, SqrtWrk


class SqrtCalculator(QMainWindow):
    # инициализация графического интерфейса
    def __init__(self):
        super(SqrtCalculator, self).__init__()
        loadUi('form.ui', self)
        self.calculateBtn.clicked.connect(self.calculate)
        self.russianBtn.clicked.connect(lambda: self.labelChanged(True))
        self.englishBtn.clicked.connect(lambda: self.labelChanged(False))

    def labelChanged(self, state):
        self.labelRound.setText("Округление" if state else "Round")

    def calculate(self):
        number = isMatch(self.enter.text())
        self.answer.setText(str(SqrtWrk(number, self.spinBox.value())))


app = QApplication(sys.argv)
mainwindow = SqrtCalculator()
widget = QtWidgets.QStackedWidget()
widget.setFixedHeight(160)
widget.setFixedWidth(450)
widget.addWidget(mainwindow)
widget.show()
sys.exit(app.exec_())
