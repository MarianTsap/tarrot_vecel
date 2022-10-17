#%%
# work with MySQL
#pip install mysql-connector-python
# Fill database table data
import mysql.connector
import sqlite3
import os
import sys
sys.path.append('F:/install/python/function/file_csv_r_w')
from maine import read_csv, write_csv

#sqlite3
#sqlite3 list tables in base
def sql_fetch(con, sql):
    cursorObj = con.cursor()
    cursorObj.execute(sql)
    #print(cursorObj.fetchall())
    for item in cursorObj.fetchall():
        print(item[0])
# drop table
def sql_drop(con):
    cursorObj = con.cursor()
    cursorObj.execute('DROP table if exists rooms_room')
    print(cursorObj.fetchall())
    
# insert table
def sql_insert(con, card, card_meaning):
    cursorObj = con.cursor()
    sql = 'INSERT INTO cards_cards(card, card_meaning) VALUES(?,?)'
    val = (card, card_meaning)
    cursorObj.execute(sql, val)
    con.commit()

# update table
def sql_update(con, card_meaning_ukr, ID):
    cursorObj = con.cursor()
    sql = 'UPDATE cards_cards SET card_meaning_ukr = ? WHERE ID = ?'
    val = (card_meaning_ukr, ID)
    cursorObj.execute(sql, val)
    con.commit()


#sqlite3
base_dir = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(base_dir,'db.sqlite3')

con = sqlite3.connect(file_path)
#sql = 'SELECT name from sqlite_master where type= "table"' # name all tables
#sql = ' SELECT ID, card_meaning_ukr FROM cards_cards'  # table structure
#sql_fetch(con,sql)


list_ukr = read_csv(r"F:/install/python/tarrot/source_meaning/text_meaning_ukr.csv")
for i in range(1,79):
    sql_update(con,list_ukr[i-1],i)
    #print(item)

sql = ' SELECT card_meaning_ukr FROM cards_cards'  # table structure
sql_fetch(con,sql)

con.close()






