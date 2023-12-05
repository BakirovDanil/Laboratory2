from abc import ABC
from tkinter import ttk


class Figure(ABC):  # создание класса (в данном случае класс абстрактный)

    def Sozdanie(self, window):  # создание метода класса
        pass  # заглушка (то есть метод ничего не делает)


def on_key_press(event):  # функция для проверки корректности ввода
    if event.char.lower() not in ['.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                                  '\x08']:  # если при нажатии клавиши на клавиатуре, нажатого символа нет в списке, то ввод не производится
        return "break"  # вернуть break (то есть ничего не делать)
    elif event.char == '.' in event.widget.get():  # если точка уже бьла введена, то повтороно ввести нельзя будет
        return "break"  # вернуть break (то есть ничего не делать)


class Label(Figure):  # создание класса который является наследником от класса Figure

    def Sozdanie(self, window):  # создание функции для создания и размещения объектов типа Label
        summaLabel = ttk.Label(text="Сумма кредита:")  # создание объекта типа Label с заданным параметром (text)
        srokLabel = ttk.Label(text="Срок кредита:")  # создание объекта типа Label с заданным параметром (text)
        stavkaLabel = ttk.Label(text="Ключевая ставка:")  # создание объекта типа Label с заданным параметром (text)
        typeLabel = ttk.Label(
            text="Тип ежемесячных платежей:")  # создание объекта типа Label с заданным параметром (text)
        EveryMonthLabel = ttk.Label(
            text="Ежемесячный платеж")  # создание объекта типа Label с заданным параметром (text)
        ProcentLabel = ttk.Label(
            text="Начисленные проценты")  # создание объекта типа Label с заданным параметром (text)
        DolgLabel = ttk.Label(text="Сумма долга")  # создание объекта типа Label с заданным параметром (text)
        summaLabel.place(x=25, y=25)  # размещение метки в окне (Сумма кредита)
        srokLabel.place(x=25, y=60)  # размещение метки в окне (Срок кредита)
        stavkaLabel.place(x=25, y=95)  # размещение метки в окне (Ключевая ставка)
        typeLabel.place(x=25, y=150)  # размещение метки в окне (Тип ежемесячных платежей)
        EveryMonthLabel.place(x=25, y=260)  # размещение метки в окне (Ежемесячгый платеж)
        ProcentLabel.place(x=25, y=295)  # размещение метки в окне (Начисленные проценты)
        DolgLabel.place(x=25, y=330)  # размещение метки в окне (Сумма долга)(000)


class Entry(Figure):  # создание класса который является наследником от класса Figure
    def __init__(self, summa, srok, stavka, EveryMonth, Procent, Dolg):  # создание конструктора
        # self - указание на объекты, которые используются внутри класса\метода
        self.summa = summa
        self.srok = srok
        self.stavka = stavka
        self.EveryMonth = EveryMonth
        self.Procent = Procent
        self.Dolg = Dolg

    def Sozdanie(self, window):  # создание функции для создания и размещения объектов типа Entry
        entr1 = ttk.Entry(width=10, textvariable=self.summa)  # создание объекта типа Entry с заданным параметром (
        # width - ширина, textvariable - с какой переменной он связан)
        entr2 = ttk.Entry(width=10, textvariable=self.srok)  # создание объекта типа Entry с заданным параметром (
        # width - ширина, textvariable - с какой переменной он связан)
        entr3 = ttk.Entry(width=10, textvariable=self.stavka)  # создание объекта типа Entry с заданным параметром (
        # width - ширина, textvariable - с какой переменной он связан)
        entr4 = ttk.Entry(width=10, textvariable=self.EveryMonth, state="readonly")  # создание объекта типа Entry с
        # заданным параметром (width - ширина, textvariable - с какой переменной он связан, state - "readonly",
        # можно только читать, писать в него нельзя)
        entr5 = ttk.Entry(width=10, textvariable=self.Procent, state="readonly")  # создание объекта типа Entry с
        # заданным параметром (width - ширина, textvariable - с какой переменной он связан, state - "readonly",
        # можно только читать, писать в него нельзя)
        entr6 = ttk.Entry(width=10, textvariable=self.Dolg, state="readonly")# создание объекта типа Entry с
        # заданным параметром (width - ширина, textvariable - с какой переменной он связан, state - "readonly",
        # можно только читать, писать в него нельзя)
        entr1.place(x=185, y=25)  # размещение объекта в окне
        entr1.bind("<Key>", on_key_press)  # указание на то, какая функция вызывается при вводе с клавиатуры
        entr2.place(x=185, y=60)  # размещение объекта в окне
        entr2.bind("<Key>", on_key_press)  # указание на то, какая функция вызывается при вводе с клавиатуры
        entr3.place(x=185, y=95)  # размещение объекта в окне
        entr3.bind("<Key>", on_key_press)  # указание на то, какая функция вызывается при вводе с клавиатуры
        entr4.place(x=200, y=260)  # размещение объекта в окне
        entr4.bind("<Key>", on_key_press)  # указание на то, какая функция вызывается при вводе с клавиатуры
        entr5.place(x=200, y=295)  # размещение объекта в окне
        entr5.bind("<Key>", on_key_press)  # указание на то, какая функция вызывается при вводе с клавиатуры
        entr6.place(x=200, y=330)  # размещение объекта в окне
        entr6.bind("<Key>", on_key_press)  # указание на то, какая функция вызывается при вводе с клавиатуры


class RadioButton(Figure): # создание класса который является наследником от класса Figure
    def __init__(self, r_var): # создание конструктора
        # self - указание на объекты, которые используются внутри класса\метода
        self.r_var = r_var

    def Sozdanie(self, window): # создание функции для создания и размещения объектов типа RadioButton
        annuit = ttk.Radiobutton(text="Аннуитетные платежи", variable=self.r_var, value=0)  # создание объекта типа
        # RadioButton с заданным параметром (
        # text - текст, variable - с какой переменной он связан, value - какое значение ему соответствует)
        differenc = ttk.Radiobutton(text="Дифференцированные платежи", variable=self.r_var, value=1)  # создание
        # объекта типа RadioButton с заданным параметром (text - текст, variable - с какой переменной он связан,
        # value - какое значение ему соответствует)
        annuit.place(x=25, y=185)  # размещение объекта в окне
        differenc.place(x=25, y=220)  # размещение объекта в окне

