import locale
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog,QApplication,QMainWindow
from PyQt5.uic import loadUi
from tkinter import *
from tkinter.ttk import Combobox

class SqrtCalculator(QMainWindow):
    def __init__(self):
        super(SqrtCalculator,self).__init__()
        loadUi('form.ui',self)
        self.calculateBtn.clicked.connect(self.calculate)
        self.russianBtn.clicked.connect(lambda: self.labelChanged(True))
        self.englishBtn.clicked.connect(lambda: self.labelChanged(False))

    def isMatch(self, inputNum):  # проверка типа входных данных
        pointer = 0
        #string = string.replace(" ", "")  # удаляем пробелы, мешающие работе
        inputNum = inputNum.replace('i', 'j')  # приводим к питон-виду, если есть комплексная часть
        try:  # int, ноль
            if (inputNum.find('-') != -1 and inputNum.find('j') == -1):
                inputNum += '+0j'
            inputNum = int(inputNum)
            inputNum = 1
        except (ValueError, TypeError):

            try:  # float
                inputNum = locale.atof(inputNum)
                pointer = 2
            except (ValueError, TypeError):

                try:  # комплексное число
                    inputNum = complex(inputNum)
                    pointer = 3
                except (ValueError, TypeError):
                    inputNum = "Error"
        return [pointer, inputNum]

    def SqrtWrk(self, number, rounder=2):  # вычисление корня
        temp = '±'

        if (number[0] == 1 or number[0] == 2):
            # int, ноль или float
            temp += str(
                round(pow(number[1], 0.5), rounder))

        elif (number[0] == 3):
            # комплексное число
            compTemp = pow(number[1], 0.5)  # находим корень
            temp += str(round(compTemp.real, rounder) + round(compTemp.imag, rounder) * 1j)

        else:
            temp = number[1]

        return temp

    def labelChanged(self, state):
        self.labelRound.setText("Округление" if state==True else "Round")

    def calculate(self):
        number = self.isMatch(self.enter.text())
        self.answer.setText(str(self.SqrtWrk(number,self.spinBox.value())))


app=QApplication(sys.argv)
mainwindow=SqrtCalculator()
widget=QtWidgets.QStackedWidget()
widget.setFixedHeight(160)
widget.setFixedWidth(450)
widget.addWidget(mainwindow)
widget.show()
sys.exit(app.exec_())
