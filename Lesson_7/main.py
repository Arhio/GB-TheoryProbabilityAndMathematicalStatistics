import numpy as np
from scipy.stats.stats import pearsonr
import pandas as pd
from pydoc import help


class Lesson_7:
    def Slope_b(self, X:[], y:[]):
        return (np.mean(X * y) - np.mean(X) * np.mean(y))/(np.mean(X**2) - np.mean(X)**2)

    def Intercept_a(self, X:[], y:[], b:float):
        return np.mean(y) - b * np.mean(X)

    '''Метод наименьших квадратов для градиентного спуска - Без Intercept'''
    def mse_(self, B1:float, X:np.array, y:np.array, n:int):
        return np.sum((B1 * X - y)**2) / n

    '''Метод наименьших квадратов для градиентного спуска - Slope'''
    def mse_p(self, B1:float, X:np.array, y:np.array, n:int, alfa:float = 1e-6):
        return B1 - alfa * (2 / n) * np.sum((B1 * X - y) * X)

    '''Градиентный спуск без Intercept'''
    def Grad(self, X:np.array, Y:np.array, B1:float, inter:int, alfa:float = 1e-6):
        for i in range(inter):
            B1 = self.mse_p(B1, X, Y, len(X), alfa)
            if i % 10 == 0:
                print('Iteration: {i}, B1={B1}, mse={mse}'.format(i=i, B1=B1, mse=self.mse_(B1, X, Y, len(X))))

    '''Метод наименьших квадратов для градиентного спуска - c Intercept'''
    def mse_i(self,B0:float, B1: float, X: np.array, y: np.array, n: int):
        return np.sum(((B0 + B1 * X) - y) ** 2) / n

    '''Метод наименьших квадратов для градиентного спуска - Slope'''
    def mse_i_p_B0(self,B0:float, B1: float, X: np.array, y: np.array, n: int, alfa: float = 1e-6):
        return B0 - alfa * (2 / n) * np.sum((B0 + B1 * X) - y)

    '''Метод наименьших квадратов для градиентного спуска - Intercept'''
    def mse_i_p_B1(self,B0:float, B1: float, X: np.array, y: np.array, n: int, alfa: float = 1e-6):
        return B1 - alfa * (2 / n) * np.sum(((B0 + B1 * X) - y) * X)

    '''Градиентный спуск c Intercept'''
    def Grad_i(self, X: np.array, Y: np.array, B0:float, B1: float, inter: int, alfa: float = 1e-6):
        for i in range(inter):
            B0_new = self.mse_i_p_B0(B0, B1, X, Y, len(X), alfa)
            B1_new = self.mse_i_p_B1(B0, B1, X, Y, len(X), alfa)
            B0 = B0_new
            B1 = B1_new
            if i % 10 == 0:
                print('Iteration: {i}, B0={B0}, B1={B1}, mse={mse}'.format(i=i, B0=B0, B1=B1, mse=self.mse_i(B0, B1, X, Y, len(X))))

    def Task_1(self, zp:[], ks:[]):
        print('1. Даны значения величины заработной платы заемщиков банка (zp) и значения их поведенческого кредитного скоринга (ks): zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110], ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832]. Используя математические операции, посчитать коэффициенты линейной регрессии, приняв за X заработную плату (то есть, zp - признак), а за y - значения скорингового балла (то есть, ks - целевая переменная). Произвести расчет как с использованием intercept, так и без.')
        X = np.array(zp)
        Y = np.array(ks)
        n = max(len(X), len(Y))

        X_m = np.matrix(X).reshape(np.matrix(X).T.shape)
        X_ = np.hstack([np.ones(X_m.shape), X_m])
        Y_ = np.matrix(Y).reshape(np.matrix(Y).T.shape)
        B_hat = np.dot(np.linalg.inv(np.dot(X_.T, X_)), X_.T @ Y_) # с отступом
        B_hat_notInter = np.dot(np.linalg.inv(np.dot(X_m.T, X_m)), X_m.T @ Y_)[0] # без отступа

        Y_hat = B_hat_notInter * X
        mse = ((np.array(Y) - np.array(Y_hat)) ** 2).sum() / n
        print('без отступом {0}'.format(mse))


        b = self.Slope_b(X, Y)
        a = self.Intercept_a(X, Y, b)
        Y_hat = self.Intercept_a(X, Y, b) + b * X

        mse = ((Y - Y_hat) ** 2).sum() / n
        print('с отступом {0}'.format(mse))

    def Task_2(self, X: np.array, Y: np.array, B1: float, inter: int, alfa: float = 1e-6):
        print('2. Посчитать коэффициент линейной регрессии при заработной плате (zp), используя градиентный спуск (без intercept).')
        self.Grad(X, Y, B1, inter, alfa)

    def Task_3(self):
        print('В каких случаях для вычисления доверительных интервалов и проверки статистических гипотез используется таблица значений функции Лапласа, а в каких - таблица критических точек распределения Стьюдента?')
        print('Таблица функций Лапласа применяется при известных характеристиках распределения (математическое ожидание и дисперсия)')
        print('Таблица функций Стьюдента применяется при неизвестных характеристиках распределения (математическое ожидание и дисперсия) и только известен набор экспериментов.')

    def Task_4(self, X: np.array, Y: np.array, B0: float, B1: float, inter: int, alfa: float = 1e-6):
        print('*4. Произвести вычисления как в пункте 2, но с вычислением intercept. Учесть, что изменение коэффициентов должно производиться на каждом шаге одновременно (то есть изменение одного коэффициента не должно влиять на изменение другого во время одной итерации).')
        self.Grad_i(X, Y, B0, B1, inter, alfa)

if __name__ == '__main__':
    lesson = Lesson_7()
    #lesson.Grad(np.array([27,37,42,48,54,56,77,88]), np.array([1.2, 1.6,1.8, 1.8, 2.5, 2.6, 3, 3.3]), 0.1, 100)
    lesson.Task_1([27,37,42,48,54,56,77,88], [1.2, 1.6,1.8, 1.8, 2.5, 2.6, 3, 3.3])
    lesson.Task_1([35, 45, 190, 200, 40, 70, 54, 150, 120, 110], [401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
    lesson.Task_2(np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110]), np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832]), 0.1, 1000)
    lesson.Task_3()
    lesson.Task_4(np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110]),
                  np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832]), 0.1, 0.1, 5000)
    print()
