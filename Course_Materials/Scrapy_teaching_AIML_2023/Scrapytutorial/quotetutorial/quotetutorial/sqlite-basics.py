# -*- coding: utf-8 -*-

import sqlite3

conn = sqlite3.connect('myquotes.db')
curr = conn.cursor()

# curr.execute(""" create table quotes_tb(
#     title text,
#     author text,
#     tag text
#     )""")

curr.execute("""insert into quotes_tb values ('python','raghu', 'web')""")

conn.commit()
conn.close()
