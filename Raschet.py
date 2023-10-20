from abc import ABC


class Method(ABC):

    def Raschet(self, summa, srok, stavka, procent, everyMonth, dolg):
        pass


class Annuit(Method):
    def Raschet(self, summa, srok, stavka, procent, everyMonth, dolg):
        if isinstance(summa.get(), int):
            srok = srok.get() * 12
            everyMonthStavka = stavka.get() / (12 * 100)
            globalStavka = (1 + everyMonthStavka) ** srok
            everyMonth1 = int((summa.get() * everyMonthStavka * globalStavka) / (globalStavka - 1))
            procent1 = int(everyMonth1 * srok - summa.get())
            dolg2 = int(procent1 + summa.get())
            procent.set(procent1)
            everyMonth.set(everyMonth1)
            dolg.set(dolg2)
        else:
            print("Некорректное значение")


class Difference(Method):
    def Raschet(self, summa, srok, stavka, procent, everyMonth, dolg):
        global procentPart, accuredInterest, ostatok, dolg1, monthlyPayment  # данные для расчетов внутри функции
        accuredInterest = 0
        srok = srok.get() * 12  # получаем содержимое поля ввода
        everyMonthStavka = stavka.get() / (12 * 100)  # ежемесячная ставка
        everyMonthDolg = summa.get() / srok  # ежемесячнео погашение долга
        ostatok = summa.get()  # начальный остаток по платежу
        MaxEveryMonth = ostatok * everyMonthStavka + everyMonthDolg  # маскимальный платеж в первый месяц
        for i in range(1, srok + 1, 1):  # цикл до последнего месяца платежа
            procentPart = ostatok * everyMonthStavka
            monthlyPayment = procentPart + everyMonthDolg
            ostatok -= everyMonthDolg
            accuredInterest += procentPart
        dolg1 = summa.get() + accuredInterest
        MinEveryMonth = monthlyPayment
        procent.set(int(accuredInterest))
        everyMonth.set(int(MinEveryMonth))
        dolg.set(int(dolg1))

