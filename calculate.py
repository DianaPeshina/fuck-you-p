import locale


def isMatch(inputNum):  # проверка типа входных данных
    pointer = 0
    if isinstance(inputNum, str):
        inputNum = inputNum.replace(',', '.')
    try:  # int, ноль
        if isinstance(inputNum, str) and inputNum.find('-') != -1 and inputNum.find('j') == -1:
            inputNum += '+0j'
        inputNum = int(inputNum)
        pointer = 1
    except (ValueError, TypeError):

        try:  # float
            inputNum = locale.atof(inputNum)
            pointer = 2
        except (ValueError, TypeError):
            inputNum = inputNum.replace('i', 'j')  # приводим к питон-виду, если есть комплексная часть
            try:  # комплексное число
                inputNum = complex(inputNum)
                pointer = 3
            except (ValueError, TypeError):
                inputNum = "Error"
    return [pointer, inputNum]


def SqrtWrk(number, rounder=2):  # вычисление корня
    temp = '±'

    if number[0] == 1 or number[0] == 2:
        # int, ноль или float
        temp += str(
            round(pow(number[1], 0.5), rounder))

    elif number[0] == 3:
        # комплексное число
        compTemp = pow(number[1], 0.5)  # находим корень
        temp += str(round(compTemp.real, rounder) + round(compTemp.imag, rounder) * 1j)

    else:
        temp = number[1]

    return temp