# Данная часть кода служит для
# создания окна и вызова методов
# из другой части кода для размещения объектов

from tkinter import *  # импорт библиотеки tkinter
from tkinter import ttk

import Raschet  # импорт
import Figure


def MainForm(window): # функция для создания формы
    window.title("Ипотечный калькулятор для физических лиц")  # установка названия в окне
    window.iconbitmap()  # установка иконки (добавить позже)
    window.geometry("500x600+400+200")  # размер окна (ширина x высота)
    window.resizable(False, False) # запрет на изменение размера окна
    window.protocol("WM_DELETE_WINDOW", finish)  # первое - имя события, второе - вызов функции
    window.mainloop() # бесконечное отображение окна приложения


def finish(): # функция для закрытия окна
    Frame.destroy() # вызывается функция destroy на Frame (графическое окно)
    print("Закрытие приложения") # вывод надписи в терминал


Frame = Tk()  # создание графического окна (Frame - главное )

summa = IntVar() # объявление переменной типа IntVar (целочисленное значение)
srok = IntVar() # объявление переменной типа IntVar (целочисленное значение)
stavka = DoubleVar() # объявление переменной типа DoubleVar (значение с плавающей запятой)
EveryMonth = IntVar() # объявление переменной типа IntVar (целочисленное значение)
Procent = IntVar() # объявление переменной типа IntVar (целочисленное значение)
Dolg = IntVar() # объявление переменной типа IntVar (целочисленное значение)

r_var = IntVar() # объявление переменной типа IntVar (целочисленное значение). Данная переменная служит для функционирования RadioButton
r_var.set(0) # установка в переменную значения 0

def Vibor(): # функция (в зависимости от выбранного RadioButton )
    if r_var.get() == 0: # если значение ноль, то выбирается первый способ расчета
        a1 = Raschet.Annuit() # создание объекта класса
        a1.Raschet(summa, srok, stavka, Procent, EveryMonth, Dolg) # использование функции созданного объекта (в скобках передаются параметры, с которыми функция работает)
    elif r_var.get() == 1: # если значение 1, то выбирается второй способ расчета
        a2 = Raschet.Difference() # создание объекта класса
        a2.Raschet(summa, srok, stavka, Procent, EveryMonth, Dolg) # использование функции созданного объекта (в скобках передаются параметры, с которыми функция работает)


btn = ttk.Button(text="Рассчитать", command=Vibor) # создание кнопки на форме (text - это то, что отображается на кнопке, command - какое действие происходит при нажатии на кнопку)
btn.place(x=50, y=400) # размещение объекта на форме (функция place)

Label = Figure.Label() # создание объекта класса
Label.Sozdanie(Frame) # использование функции созданного объекта (в скобках параметры)
Entry = Figure.Entry(summa, srok, stavka, EveryMonth, Procent, Dolg) # создание объекта класса (в скобак передаются параметры конструктора)
Entry.Sozdanie(Frame) # использование функции созданного объекта (в скобках параметры)
RadioButton = Figure.RadioButton(r_var)#  создание объекта класса (в скобак передаются параметры конструктор
RadioButton.Sozdanie(Frame) # использование функции созданного объекта (в скобках параметры)
MainForm(Frame) # использование функции (в скобках передается параметр)
