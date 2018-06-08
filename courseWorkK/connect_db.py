import psycopg2


def connect_db():
    try:
        conn = psycopg2.connect("dbname='betting' user='postgres' host='localhost' password='blackwow'")
        return conn
    except:
        print("I am unable to connect to the database")