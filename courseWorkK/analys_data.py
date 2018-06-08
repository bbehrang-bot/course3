from connect_db import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import calendar
import filter_data as fd
PLOT_LABEL_FONT_SIZE = 8

def getColors(n):
    COLORS = []
    cm = plt.cm.get_cmap('hsv', n)
    for i in np.arange(n):
        COLORS.append(cm(i))
    return COLORS

def dict_sort(my_dict):
    keys = []
    values = []
    #my_dict = sorted(my_dict.items(), key=lambda x:x[1], reverse=True)
    for k, v in my_dict.items():
        keys.append(calendar.month_abbr[k.month])
        values.append(v)
    return (keys,values)

def dict_sort_simple(my_dict):
    keys = []
    values = []
    #my_dict = sorted(my_dict.items(), key=lambda x:x[1], reverse=True)
    for k, v in my_dict.items():
        keys.append(k)
        values.append(v)
    return (keys,values)

def total_receipt(year):
    conn = connect_db()
    df = pd.read_sql("SELECT date, (SUM(general_betting_duty)+SUM(pool_betting_duty)+SUM(gaming_duty)+SUM(amusement_machine_licence)+SUM(bingo)+SUM(machine_games_duty)+SUM(lottery_duty)) AS total FROM public.bettings where extract(year from date) = %s Group BY date" % year, conn)
    dict = {}
    for i in range(len(df.values)):
        dict[df.values[i][0]] = df.values[i][1]

    dict_keys,dict_values = dict_sort(dict)
    top_keys = len(dict_keys)
    plt.title('Total receipts for the year: %s' % year, fontsize=PLOT_LABEL_FONT_SIZE)
    plt.bar(np.arange(top_keys), dict_values, color=getColors(top_keys))
    plt.xticks(np.arange(top_keys), dict_keys, rotation=0, fontsize=8)
    plt.yticks(fontsize=PLOT_LABEL_FONT_SIZE)
    plt.ylabel('receipts €', fontsize=PLOT_LABEL_FONT_SIZE)

    plt.show()


def total_receipt_years(years):
    conn = connect_db()
    for year in years:
        df = pd.read_sql("SELECT date, (SUM(general_betting_duty)+SUM(pool_betting_duty)+SUM(gaming_duty)+SUM(amusement_machine_licence)+SUM(bingo)+SUM(machine_games_duty)+SUM(lottery_duty)) AS total FROM public.bettings where extract(year from date) = %s Group BY date" % year, conn)
        dict = {}
        for i in range(len(df.values)):
            dict[df.values[i][0]] = df.values[i][1]

        dict_keys, dict_values = dict_sort(dict)
        top_keys = len(dict_keys)
        plt.plot(dict_keys, dict_values, label='%s' % year)
    plt.title('Total receipts for the year: %s' % years, fontsize=PLOT_LABEL_FONT_SIZE)
    plt.ylabel('receipts €', fontsize=PLOT_LABEL_FONT_SIZE)
    plt.legend()
    plt.show()

# No Need
def column_year(field, year):
    conn = connect_db()
    df = pd.read_sql("SELECT date,%s FROM public.bettings where extract(year from date) = %s"% (field, year), conn)
    dict = {}
    for i in range(len(df.values)):
        dict[df.values[i][0]] = df.values[i][1]

    dict_keys, dict_values = dict_sort(dict)
    top_keys = len(dict_keys)
    plt.title('%s receipt of the year: %s' %(field, year), fontsize=PLOT_LABEL_FONT_SIZE)
    plt.bar(np.arange(top_keys), dict_values, color=getColors(top_keys))
    plt.xticks(np.arange(top_keys), dict_keys, rotation=0, fontsize=8)
    plt.yticks(fontsize=PLOT_LABEL_FONT_SIZE)
    plt.ylabel('receipt €', fontsize=PLOT_LABEL_FONT_SIZE)
    plt.show()



def column_full(field):
    conn = connect_db()
    years = fd.get_years()

    for elem in years:
        year = elem[0]
        q = ('%f' % year).rstrip('0').rstrip('.')
        df = pd.read_sql("SELECT date,%s FROM public.bettings where extract(year from date) = %s" % (field, q), conn)
        dict = {}
        for i in range(len(df.values)):
            dict[df.values[i][0]] = df.values[i][1]
        dict_keys, dict_values = dict_sort(dict)
        top_keys = len(dict_keys)
        plt.plot(dict_keys, dict_values, label="%s" %q)

    plt.title('%s from the year : %s' %(field,year), fontsize=PLOT_LABEL_FONT_SIZE)


    plt.ylabel('€', fontsize=PLOT_LABEL_FONT_SIZE)
    plt.legend()
    plt.show()

def column_multiple_years(field,years):
    conn = connect_db()

    for year in years:
        df = pd.read_sql("SELECT date,%s FROM public.bettings where extract(year from date) = %s" % (field, year), conn)
        dict = {}
        for i in range(len(df.values)):
            dict[df.values[i][0]] = df.values[i][1]
        dict_keys, dict_values = dict_sort(dict)
        top_keys = len(dict_keys)
        plt.plot(dict_keys, dict_values, label="%s" %year)


    plt.title('%s from the year : %s' %(field,years), fontsize=PLOT_LABEL_FONT_SIZE)
    plt.ylabel('€', fontsize=PLOT_LABEL_FONT_SIZE)
    plt.legend()
    plt.show()

def annual_receipt(field):
    conn = connect_db()
    years = fd.get_years()
    dict_keys = []
    dict_values = []
    for elem in years:
        year = elem[0]
        q = ('%f' % year).rstrip('0').rstrip('.')
        df = pd.read_sql(
            "SELECT sum(%s) from public.bettings where extract(year from date) = %s" % (field, q),
            conn)
        dict_keys.append(q)
        dict_values.append(df.values[0][0])
    top_keys = len(dict_keys)
    plt.title('Year by year total income of %s' %field, fontsize=PLOT_LABEL_FONT_SIZE)
    plt.bar(np.arange(top_keys), dict_values, color=getColors(top_keys))
    plt.xticks(np.arange(top_keys), dict_keys, rotation=90, fontsize=8)
    plt.yticks(fontsize=PLOT_LABEL_FONT_SIZE)
    plt.ylabel('€', fontsize=PLOT_LABEL_FONT_SIZE)
    plt.show()



def annual_betting():
    conn = connect_db()
    years = fd.get_years()
    dict_keys = []
    dict_values = []
    for elem in years:
        year = elem[0]
        q = ('%f' % year).rstrip('0').rstrip('.')
        df = pd.read_sql(
            "SELECT date,(SUM(general_betting_duty) + SUM(pool_betting_duty)) as SUM from public.bettings where extract(year from date) = %s group by date"%q,
            conn)
        dict_keys.append(q)
        sum = 0
        for i in range(len(df.values)):
            sum += (df.values[i][1])
        dict_values.append(sum)
    top_keys = len(dict_keys)
    plt.title('Betting total', fontsize=PLOT_LABEL_FONT_SIZE)
    plt.bar(np.arange(top_keys), dict_values, color=getColors(top_keys))
    plt.xticks(np.arange(top_keys), dict_keys, rotation=90, fontsize=8)
    plt.yticks(fontsize=PLOT_LABEL_FONT_SIZE)
    plt.ylabel('€', fontsize=PLOT_LABEL_FONT_SIZE)
    plt.show()

def annual_gaming():
    conn = connect_db()
    years = fd.get_years()
    dict_keys = []
    dict_values = []
    for elem in years:
        year = elem[0]
        q = ('%f' % year).rstrip('0').rstrip('.')
        df = pd.read_sql(
            "SELECT date,(SUM(gaming_duty) + SUM(amusement_machine_licence)+SUM(bingo)+SUM(machine_games_duty)) as SUM from public.bettings where extract(year from date) = %s group by date"%q,
            conn)
        dict_keys.append(q)
        sum = 0
        for i in range(len(df.values)):
            sum += (df.values[i][1])
        dict_values.append(sum)
    top_keys = len(dict_keys)
    plt.title('Gaming total', fontsize=PLOT_LABEL_FONT_SIZE)
    plt.bar(np.arange(top_keys), dict_values, color=getColors(top_keys))
    plt.xticks(np.arange(top_keys), dict_keys, rotation=90, fontsize=8)
    plt.yticks(fontsize=PLOT_LABEL_FONT_SIZE)
    plt.ylabel('€', fontsize=PLOT_LABEL_FONT_SIZE)
    plt.show()