# Данная часть кода служит для
# создания окна и вызова методов
# из другой части  кода для размещения объектов

from tkinter import *  # импорт библиотеки tkinter
from tkinter import ttk

#import Raschet  # импорт
#import Figure


def MainForm(window):
    window.title("Ипотечный калькулятор для физических лиц")  # установка названия в окне
    window.iconbitmap()  # установка иконки (добавить позже)
    window.geometry("500x600+400+200")  # размер окна (ширина x высота)
    window.resizable(False, False)
    window.protocol("WM_DELETE_WINDOW", finish)  # первое - имя события, второе - вызов функции
    window.mainloop()


def finish():
    Frame.destroy()
    print("Закрытие приложения")


Frame = Tk()  # создание графического окна

summa = IntVar()
srok = IntVar()
stavka = DoubleVar()
EveryMonth = IntVar()
Procent = IntVar()
Dolg = IntVar()

r_var = IntVar()
r_var.set(0)


#def Vibor():
    #if r_var.get() == 0:
        #прописывается функция для первого выбора radiobutton
    #elif r_var.get() == 1:
        #прописывется фнукция для второго выбора radiobutton


btn = ttk.Button(text="Рассчитать")
btn.place(x=50, y=400)

#Сюда будут вписываться функции для создания объекты на оконной форме
