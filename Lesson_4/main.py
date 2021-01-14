import pandas as pd


def Task_1(a, b):
    print('Задача 1')
    M_x = (a + b) / 2
    D_x = ((a + b) ^ 2) / 12
    print('M(x) = {0} D(x) = {1}'.format(M_x, D_x))


def Task_2(a, sigma):
    print('Задача 2')
    b = (sigma / 12)**(1/2) + a
    print('b = {0}'.format(b))


def Task_3(M_x, D_x, sigma):
    print('Задача 3')
    print('M(x) = {0}, D(x) = {1}, δ = {2}'.format(M_x, D_x, sigma))


def Task_4(M_x, sigma, tasks):
    print('Задача 4')
    Ztab = pd.read_csv('table.csv', sep=';')
    for task in tasks:
        if len(task) == 2:
            p = round((int(task[1][1]) - M_x) / sigma, 2)
            tab = Ztab.loc[Ztab['sigma'] == abs(p)]
            if len(tab) > 0:
                l = 0.5 + float(tab['Z'].values[0]) if p > 0 else 0.5 - float(tab['Z'].values[0])
                if task[1][0] == '>=':
                    print('При {0}: δ = {1}, P = {2}%'.format(task[0], p, round((1 - l) * 100.0, 2)))
                elif task[1][0] == '<=':
                    print('При {0}: δ = {1}, P = {2}%'.format(task[0], p, round(l * 100.0, 2)))
        elif len(task) == 3:
            p1 = round((int(task[1][1]) - M_x) / sigma, 2)
            p2 = round((int(task[2][1]) - M_x) / sigma, 2)
            tab1 = Ztab.loc[Ztab['sigma'] == abs(p1)]
            tab2 = Ztab.loc[Ztab['sigma'] == abs(p2)]

            if len(tab1) > 0 and len(tab2) > 0:
                l1 = 0.5 + tab1['Z'].values[0] if p1 > 0 else 0.5 - tab1['Z'].values[0]
                l2 = 0.5 + tab2['Z'].values[0] if p2 > 0 else 0.5 - tab1['Z'].values[0]

                if task[1][0] == '<=' and task[2][0] == '>=':
                    print('При {0}: δ₁ = {1}, δ₂ = {2}, P = {3}%'.format(task[0], p1, p2, round((l1 + (1 - l2)) * 100, 2)))
                elif task[1][0] == '>=' and task[2][0] == '<=':
                    print('При {0}: δ₁ = {1}, δ₂ = {2}, P = {3}%'.format(task[0], p1, p2, round((l2 - l1) * 100, 2)))

def Task_5(M_x, D_x, val):
    print('Задача 5')
    print('δ = {0}'.format((val - M_x)/(D_x**(1/2))))


if __name__ == '__main__':
    Task_1(200, 800)
    Task_2(0.5, 0.2)
    Task_3(2, 16, 4)
    Task_4(174, 8, [['больше 182 мм', ('>=', 182)], ['больше 190 мм', ('>=', 190)], ['от 166 до 190 мм', ('>=', 166), ('<=', 190)], ['от 166 до 182 мм', ('>=', 166), ('<=', 182)], ['не выше 150 мм или не ниже 190 мм', ('<=', 150), ('>=', 190)], ['не выше 150 мм или не ниже 198 мм', ('<=', 150), ('>=', 198)], ['ниже 166 мм', ('<=', 166)]])
    Task_5(178, 25, 190)
