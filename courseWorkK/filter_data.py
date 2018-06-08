from connect_db import *

def filter_data(column,value):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM public.bettings WHERE %s=$$%s$$" % (column, value))
    res = cursor.fetchall()
    for elem in res:
        print(elem)

def filter_data_gt(column,value):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM public.bettings WHERE %s>$$%s$$" % (column, value))
    res = cursor.fetchall()
    for elem in res:
        print(elem)

def filter_data_ls(column,value):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM public.bettings WHERE %s<$$%s$$" % (column, value))
    res = cursor.fetchall()
    for elem in res:
        print(elem)

def filter_date(field, value):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM public.bettings WHERE EXTRACT(%s FROM date)=$$%s$$" % (field,value))
    res = cursor.fetchall()
    for elem in res:
        print(elem)

def filter_date_ls(field, value):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM public.bettings WHERE EXTRACT(%s FROM date)<$$%s$$" % (field,value))
    res = cursor.fetchall()
    for elem in res:
        print(elem)

def filter_date_gt(field, value):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM public.bettings WHERE EXTRACT(%s FROM date)>$$%s$$" % (field, value))
    res = cursor.fetchall()
    for elem in res:
        print(elem)

def get_years():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("select distinct date_part('year',date) from public.bettings order by date_part asc")
    res = cursor.fetchall()
    return res

