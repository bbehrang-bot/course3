from connect_db import *
import random
import pandas as pd
import numpy as np
def generate_data(year):

    conn = connect_db()
    cur = conn.cursor()

    if year > 1995 and year < 2018:
        for i in range(year, 2018):
            for j in range(1, 13):
                general_betting_duty = random.randint(21099, 47720853)
                pool_betting_duty = random.randint(4457, 661077)
                gaming_duty = random.randint(54064, 1825736)
                amusement_machine_licence = random.randint(246183, 6973815)
                bingo = random.randint(246183, 6973815)
                machine_games_duty = random.randint(246183, 6973815)
                lottery_duty = random.randint(246183, 6973815)
                date = '%s-%s-01' % (i, j)
                cur.execute(
                    'INSERT INTO public.bettings(date, general_betting_duty, pool_betting_duty, gaming_duty, amusement_machine_licence,bingo,machine_games_duty,lottery_duty) '
                    'VALUES(%s, %s, %s, %s, %s, %s, %s, %s)',
                    (date, general_betting_duty, pool_betting_duty, gaming_duty, amusement_machine_licence,bingo,machine_games_duty,lottery_duty ))
        conn.commit()


def read_data():
    file = 'dataset.xlsx'

    xl = pd.ExcelFile(file)

    df1 = xl.parse('Sheet1')
    conn = connect_db()
    cursor = conn.cursor()
    for i in range(0, len(df1)):
        try:
            date = df1.Time[i]
            general_betting_duty = np.int(df1.general_betting_duty[i])
            pool_betting_duty = np.int(df1.pool_betting_duty[i])
            gaming_duty = np.int(df1.gaming_duty[i])
            amusement_machine_licence = np.int(df1.amusement_machine_licence[i])
            bingo = np.int(df1.bingo[i])
            machine_games_duty = np.int(df1.machine_games_duty[i])
            lottery_duty = np.int(df1.lottery_duty[i])
            cursor.execute(
                'INSERT INTO public.bettings(date, general_betting_duty, pool_betting_duty, gaming_duty, amusement_machine_licence,bingo,machine_games_duty,lottery_duty) '
                'VALUES(%s, %s, %s, %s, %s, %s, %s, %s)',
                (date, general_betting_duty, pool_betting_duty, gaming_duty, amusement_machine_licence, bingo,
                 machine_games_duty, lottery_duty))
            conn.commit()
        except ValueError:
            continue
    print("done")