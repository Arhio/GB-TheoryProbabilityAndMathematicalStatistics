import numpy as np
from scipy.stats.stats import pearsonr
import pandas as pd
from pydoc import help

class Lesson_6:
    def Task_1(self, zp:[], ks:[]):
        print('Даны значения величины заработной платы заемщиков банка (zp) и значения их поведенческого кредитного скоринга (ks):'
              'zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110],'
              'ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832].'
              'Найдите ковариацию этих двух величин с помощью элементарных действий, а затем с помощью функции cov из numpy'
              'Полученные значения должны быть равны.'
              'Найдите коэффициент корреляции Пирсона с помощью ковариации и среднеквадратичных отклонений двух признаков,'
              'а затем с использованием функций из библиотек numpy и pandas.')
        zp = np.array(zp)
        ks = np.array(ks)
        np.corrcoef(zp, ks)# коэффициент корреляции

        c = round(np.mean(zp * ks) - np.mean(zp) * np.mean(ks), 10)
        covariachia = np.cov(zp, ks, ddof=0)
        sigma_zp = np.std(zp, ddof=0)
        sigma_ks = np.std(ks, ddof=0)
        covPirsona1 = c / (sigma_zp * sigma_ks)
        covPirsona2 = covariachia[0, 1] / (sigma_zp * sigma_ks)
        covPirsona3 = pearsonr(zp, ks)
        print('')

    def Task_2(self, exp:[], a:float):
        print('Измерены значения IQ выборки студентов,'
              'обучающихся в местных технических вузах:'
              '131, 125, 115, 122, 131, 115, 107, 99, 125, 111.'
              'Известно, что в генеральной совокупности IQ распределен нормально.'
              'Найдите доверительный интервал для математического ожидания с надежностью 0.95.')

        Stu_tab = pd.read_csv('tableStiudent.csv', sep=';')

        a_2 = round((1-a) / 2, 4)

        t_a_2 = Stu_tab[str(a_2)][(Stu_tab['v'] - len(exp) - 1).abs().argsort()[:1]].to_list()[0]
        X_hat = np.asarray(exp).mean()
        sigma = np.std(exp, ddof=1)
        T_neg = round(X_hat - t_a_2 * (sigma/(len(exp)**(1/2))), 3)
        T_pos = round(X_hat + t_a_2 * (sigma/(len(exp)**(1/2))), 3)

        print('[{0},{1}]'.format(T_pos, T_neg))
        print('Выборка не репрезентативна в силу малого объема выборки')

    def Task_3(self, sigma:float, M:float, n:int, a:float):
        print('Известно, что рост футболистов в сборной распределен нормально'
            'с дисперсией генеральной совокупности, равной 25 кв.см. Объем выборки равен 27,'
            'среднее выборочное составляет 174.2. Найдите доверительный интервал для математического'
            'ожидания с надежностью 0.95.')
        Ztab = pd.read_csv('Z_table.csv', sep=';')
        neg = (1 - a)/2
        pos = 1 - neg
        Z_n = Ztab.sigma[(abs(Ztab['Z'] - 0.5) - neg).abs().argsort()[:1]].to_list()[0]
        Z_p = Ztab.sigma[(Ztab['Z'] + 0.5 - pos).abs().argsort()[:1]].to_list()[0]
        X_hat = M
        Z_pos = round(X_hat - Z_n * sigma/(n**(1/2)), 3)
        Z_neg = round(X_hat + Z_p * sigma/(n**(1/2)), 3)

        print('[{0},{1}]'.format(Z_pos, Z_neg))


if __name__ == '__main__':
    lesson = Lesson_6()
    lesson.Task_1([35, 45, 190, 200, 40, 70, 54, 150, 120, 110], [401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
    lesson.Task_2([131, 125, 115, 122, 131, 115, 107, 99, 125, 111], 0.95)
    lesson.Task_3(25, 174.2, 27, 0.95)



