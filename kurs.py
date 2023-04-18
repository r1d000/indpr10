import sqlite3 as sq
from random import randrange



def fantasy():
    with sq.connect("cont.db") as con:
        cur = con.cursor()
        cur.execute("""SELECT * FROM main WHERE genre = 'фэнтези' """)
        resault = cur.fetchall()
        return resault[randrange(0, len(resault))]

def criminal():
    with sq.connect("cont.db") as con:
        cur = con.cursor()
        cur.execute("""SELECT * FROM main WHERE genre = 'криминал' """)
        resault = cur.fetchall()
        return resault[randrange(0, len(resault))]

def history():
    with sq.connect("cont.db") as con:
        cur = con.cursor()
        cur.execute("""SELECT * FROM main WHERE genre = 'история' """)
        resault = cur.fetchall()
        return resault[randrange(0, len(resault))]

def fantastic():
    with sq.connect("cont.db") as con:
        cur = con.cursor()
        cur.execute("""SELECT * FROM main WHERE genre = 'фантастика' """)
        resault = cur.fetchall()
        return resault[randrange(0, len(resault))]

def thriller():
    with sq.connect("cont.db") as con:
        cur = con.cursor()
        cur.execute("""SELECT * FROM main WHERE genre = 'триллер' """)
        resault = cur.fetchall()
        return resault[randrange(0, len(resault))]

def drama():
    with sq.connect("cont.db") as con:
        cur = con.cursor()
        cur.execute("""SELECT * FROM main WHERE genre = 'драма' """)
        resault = cur.fetchall()
        return resault[randrange(0, len(resault))]

def comedy():
    with sq.connect("cont.db") as con:
        cur = con.cursor()
        cur.execute("""SELECT * FROM main WHERE genre = 'комедия' """)
        resault = cur.fetchall()
        return resault[randrange(0, len(resault))]


if __name__ == '__main__':
    print(fantasy())
