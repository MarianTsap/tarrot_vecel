# -*- coding: utf-8 -*-
# importing psycopg2 module
import psycopg2
import pandas as pd
import sqlite3
import math
import os

# Import from sqlite3
base_dir= os.path.dirname(os.path.realpath(__file__))
con = sqlite3.connect(os.path.join(base_dir,'db.sqlite3'))
sql = 'SELECT * from cards_cards'
df = pd.read_sql(sql, con)
df = df[['id', 'card', 'card_meaning', 'card_meaning_ukr']]
#df['parent_id'] = round(df['parent_id'],0)
#df.to_csv('work.csv', index = False, header= True)
# change nan to 1
'''
for item in df.index[0:]:
    if math.isnan(df.loc[item]['parent_id']):
        df.loc[item,'parent_id']=1
'''
print(df)    
con.close()


# list that contain records to be inserted into table
df=df.loc[0:]
data=df.values.tolist()
print(data)



# Write to postgre
# establishing the connection
conn = psycopg2.connect(
	database="dpzmihkn",
	user='dpzmihkn',
	password='0K9sKINCNsoI37cY0LDwBi9MiMj4fRjN',
	host='mouse.db.elephantsql.com',
	port='5432'
)
# creating a cursor object
cursor = conn.cursor()

# inserting record into employee table
for d in data[0:]:
    #if not math.isnan(d[3]):
    cursor.execute("INSERT into cards_cards(id, card, card_meaning, card_meaning_ukr) VALUES (%s, %s, %s, %s)", d)


print("List has been inserted to employee table successfully...")

# Commit your changes in the database
conn.commit()

# Closing the connection
conn.close()

