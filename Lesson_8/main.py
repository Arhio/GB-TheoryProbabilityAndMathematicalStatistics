import pandas as pd


class Lesson_8:
    def Task_1(self, y:[[]]):
        print('Провести дисперсионный анализ для определения того, есть ли различия среднего роста среди взрослых футболистов, хоккеистов и штангистов. Даны значения роста в трех группах случайно выбранных спортсменов: Футболисты: 173, 175, 180, 178, 177, 185, 183, 182. Хоккеисты: 177, 179, 180, 188, 177, 172, 171, 184, 180. Штангисты: 172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170.')
        F_crit_tab = pd.read_csv('F_crit_Fishera_Snedcora_a_0,05.csv', sep=';')

        k = len(y)
        n = [len(e) for e in y]

        y_hat = [sum(e)/n[pos] for pos, e in enumerate(y)]

        Y_hat = sum([sum(e) for e in y]) / sum(n)
        S_2 = sum([sum([(f - Y_hat)**2 for f in e]) for e in y])
        Sf_2 = sum([n[pos] * (e - Y_hat)**2 for pos, e in enumerate(y_hat)])
        S_oct_2 = sum([sum([(f - y_hat[pos])**2 for f in e]) for pos, e in enumerate(y)])
        isS_2valid = (Sf_2 + S_oct_2) == S_2
        sigma_F_2 = Sf_2 / (k - 1)
        sigma_ost_2 = S_oct_2 / (sum(n) - k)
        F_H = sigma_F_2 / sigma_ost_2

        df_merge = round(k - 1)
        df_merge = 1 if df_merge < 1 else (12 if df_merge > 29 else df_merge)
        df_inner = round(sum(n) - k)
        df_inner = 1 if df_inner < 1 else (17 if df_inner > 61 else df_inner)

        F_crit = F_crit_tab[str(df_merge)][(F_crit_tab['v2'] - df_inner).abs().argsort()[:1]].to_list()[0]

        if F_H > F_crit:
            print('Различие между группами статистически значимое')
            return True
        else:
            print('Различие между группами статистически не значемо или не существует')
            return False

if __name__ == '__main__':
    lesson = Lesson_8()
    #lesson.Task_1([[70, 50, 65, 60, 75], [80, 75, 90, 70, 75, 65, 85, 100], [130, 100, 140, 150, 160, 170, 200]])
    lesson.Task_1([[173, 175, 180, 178, 177, 185, 183, 182],
                   [177, 179, 180, 188, 177, 172, 171, 184, 180],
                   [172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170]])


