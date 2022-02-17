import locale
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog,QApplication,QFileDialog
from PyQt5.uic import loadUi
from tkinter import *
from tkinter.ttk import Combobox


def main():
    LANGUAGE = {'RU':
                    ['Поиск корня', 'Поле для ввода', 'Поле для ответа', 'Нажать, чтоб посчитать корни', 'Округление',
                     'Язык', 'Русский', 'English', 'Deutsche',
                     'Неверный ввод'],
                'EN': ['Root searching', 'Input field', 'Output field', 'Push to take roots', 'Round', 'Language',
                       'Русский', 'English', 'Deutsche',
                       'Invalid input'],
                'DE': ['Wurzelsuche', 'Eingabefeld', 'Antwortfeld', 'Klicken Sie, um die Wurzeln zu zählen', 'Rundung',
                       'Zunge', 'Русский', 'Englisch', 'Deutsche',
                       'Ungültige Eingabe']
                }

    def calculate():
        e2.configure(state='normal')
        e2.delete(0, 'end')
        input = e1.get()  # чтение входных данных
        result = (SqrtWrk(isMatch(input), int(spin.get())))  # расчёт результата
        e2.insert(0, result)  # вывод результата
        e2.configure(state='disabled')

    def update_language(event):  # замена языка интерфейса на выбранный пользователем

        input = event.widget.current()
        lang_map = {'0': 'RU', '1': 'EN', '2': 'DE'}
        new_language = lang_map[str(input)]

        root.title(LANGUAGE[new_language][0])
        l0.config(text=LANGUAGE[new_language][5])
        l1.config(text=LANGUAGE[new_language][1])
        l2.config(text=LANGUAGE[new_language][2])
        b1.config(text=LANGUAGE[new_language][3])
        l3.config(text=LANGUAGE[new_language][4])
        combo.config(
            values=(LANGUAGE[new_language][6], LANGUAGE[new_language][7], LANGUAGE[new_language][8]))

        root.update()

    current_language = 'RU'

    root = Tk()
    root.title(LANGUAGE[current_language][0])
    f_top = Frame(root)
    f_bot = Frame(root)

    l0 = Label(f_top, text=LANGUAGE[current_language][5])
    l0.pack(side=LEFT)

    combo = Combobox(f_top, state="readonly")
    combo['values'] = (LANGUAGE[current_language][6], LANGUAGE[current_language][7], LANGUAGE[current_language][8])
    combo.current(0)
    combo.pack(side=RIGHT)
    combo.bind("<<ComboboxSelected>>", update_language)

    l1 = Label(f_bot, text=LANGUAGE[current_language][1])
    l1.pack()
    e1 = Entry(f_bot, width=50)
    e1.pack()
    l2 = Label(f_bot, text=LANGUAGE[current_language][2])
    l2.pack()
    e2 = Entry(f_bot, width=50)
    e2.configure(disabledbackground="white", disabledforeground="black")
    e2.configure(state='disabled')
    e2.pack()
    b1 = Button(f_bot, text=LANGUAGE[current_language][3])
    b1.config(command=calculate)
    b1.pack(side=LEFT)
    spin = Spinbox(f_bot, from_=0, to=100)
    spin.pack(side=RIGHT)
    l3 = Label(f_bot, text=LANGUAGE[current_language][4])
    l3.pack(side=LEFT)

    f_top.pack()
    f_bot.pack()

    root.update_idletasks()
    s = root.geometry()
    s = s.split('+')
    s = s[0].split('x')

    # установление окна по центру экрана
    w = root.winfo_screenwidth() // 2 - int(s[0]) // 2
    h = root.winfo_screenheight() // 2 - int(s[1]) // 2

    root.geometry('+{}+{}'.format(w, h))

    root.mainloop()


def isMatch(string):  # проверка типа входных данных
    pointer = 0
    #string = string.replace(" ", "")  # удаляем пробелы, мешающие работе
    
    string = string.replace('i', 'j')  # приводим к питон-виду, если есть комплексная часть
    try:  # int, ноль
        if (string.find('-') != -1 and string.find('j') == -1):
            string += '+0j'
        string = int(string)
        pointer = 1
    except (ValueError, TypeError):

        try:  # float
            string = locale.atof(string)
            pointer = 2
        except (ValueError, TypeError):

            try:  # комплексное число
                string = complex(string)
                pointer = 3
            except (ValueError, TypeError):
                string = "Error"
    return [pointer, string]


def SqrtWrk(number, rounder=2):  # вычисление корня
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


if __name__ == '__main__':
    main()
