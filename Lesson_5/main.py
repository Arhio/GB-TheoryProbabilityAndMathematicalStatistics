import numpy as np
import pandas as pd


class Lesson_5:
    def Task_1(self, sigma:float, M:float, n:int, a:float):
        print('1. Известно, что генеральная совокупность распределена нормально со средним квадратическим отклонением, равным 16. ' \
        'Найти доверительный интервал для оценки математического ожидания a с надежностью 0.95, если выборочная средняя M = 80, а объем выборки n = 256.')
        Ztab = pd.read_csv('Z_table.csv', sep=';')
        neg = (1 - a)/2
        pos = 1 - neg
        Z_n = Ztab.sigma[(abs(Ztab['Z'] - 0.5) - neg).abs().argsort()[:1]].to_list()[0]
        Z_p = Ztab.sigma[(Ztab['Z'] + 0.5 - pos).abs().argsort()[:1]].to_list()[0]
        X_hat = M
        Z_pos = round(X_hat - Z_n * sigma/(n**(1/2)), 3)
        Z_neg = round(X_hat + Z_p * sigma/(n**(1/2)), 3)

        print('[{0},{1}]'.format(Z_pos, Z_neg))


    def Task_2(self, exp:[], a:float):
        print('2. В результате 10 независимых измерений некоторой величины X, выполненных с одинаковой точностью, получены опытные данные: '
              '6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1 Предполагая, что результаты измерений подчинены нормальному закону '
              'распределения вероятностей, оценить истинное значение величины X при помощи доверительного интервала, покрывающего это значение '
              'с доверительной вероятностью 0,95. 3,4 задачи решать через тестирование гипотезы')
        Stu_tab = pd.read_csv('tableStiudent.csv', sep=';')

        a_2 = round((1-a) / 2, 4)

        t_a_2 = Stu_tab[str(a_2)][(Stu_tab['v'] - len(exp) - 1).abs().argsort()[:1]].to_list()[0]
        X_hat = np.asarray(exp).mean()
        sigma = np.std(exp, ddof=1)
        T_neg = round(X_hat - t_a_2 * (sigma/(len(exp)**(1/2))), 3)
        T_pos = round(X_hat + t_a_2 * (sigma/(len(exp)**(1/2))), 3)

        print('[{0},{1}]'.format(T_pos, T_neg))


    def Task_3(self, diam:float, mean_diam:float, Disp:float, a:float, n:int):
        print('3. Утверждается, что шарики для подшипников, изготовленные автоматическим станком, имеют средний диаметр 17 мм. '
              'Используя односторонний критерий с α=0,05, проверить эту гипотезу, если в выборке из n=100 шариков средний диаметр '
              'оказался равным 17.5 мм, а дисперсия известна и равна 4 кв.мм.')

        sigma = Disp ** (1/2)
        Ztab = pd.read_csv('Z_table.csv', sep=';')
        Z_p = Ztab.sigma[(Ztab['Z'] + 0.5 - (1 - a)).abs().argsort()[:1]].to_list()[0]

        Z = (mean_diam - diam) / (sigma / (n ** (1/2)))

        if Z_p < Z:
            print('Альтернативная гипотиза принимается, а основная отвергается')
        else:
            print('Принимается основная в силу невозможности ее отвергуть')


    def Task_4(self, weith, exp:[], a):
        print('4. Продавец утверждает, что средний вес пачки печенья составляет 200 г. '
                'Из партии извлечена выборка из 10 пачек. Вес каждой пачки составляет: '
                '202, 203, 199, 197, 195, 201, 200, 204, 194, 190. '
                'Известно, что их веса распределены нормально. ' 
                'Верно ли утверждение продавца, если учитывать, что доверительная вероятность равна 99%?')
        Stu_tab = pd.read_csv('tableStiudent.csv', sep=';')

        X_hat = np.asarray(exp).mean()
        sigma = np.std(exp, ddof=1)

        a = round((1 - a), 4)

        t_a = Stu_tab[str(a)][(Stu_tab['v'] - len(exp) - 1).abs().argsort()[:1]].to_list()[0]

        T_neg = round(X_hat - t_a * (sigma / (len(exp) ** (1 / 2))), 3)
        T_pos = round(X_hat + t_a * (sigma / (len(exp) ** (1 / 2))), 3)

        print('По доверительныйм интервалам')
        if T_neg <= weith and weith <= T_pos:
            print('Принимается основная в силу невозможности ее отвергуть')
        else:
            print('Альтернативная гипотиза принимается. Основная отвергается')

        Ztab = pd.read_csv('Z_table.csv', sep=';')
        Z_p = -Ztab.sigma[(Ztab['Z'] + 0.5 - (1 - a)).abs().argsort()[:1]].to_list()[0]
        Z = round((X_hat - weith) / (sigma / (len(exp) ** (1/2))), 4)

        print('Тестирование гипотизы')
        if Z_p > Z:
            print('Альтернативная гипотиза принимается, а основная отвергается')
        else:
            print('Принимается основная в силу невозможности ее отвергуть')


if __name__ == '__main__':
    lesson = Lesson_5
    'При известной генеральной совокупности'
    lesson.Task_1(lesson, 16, 80, 256, 0.95)

    lesson.Task_1(lesson, 5, 24.15, 100, 0.95)
    'При неизвесной генеральной совокпности'
    lesson.Task_2(lesson, [6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1], 0.95)
    ''
    lesson.Task_3(lesson, 17, 17.5, 4, 0.05, 100)
    lesson.Task_4(lesson, 200, [202, 203, 199, 197, 195, 201, 200, 204, 194, 190], 0.99)


