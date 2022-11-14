#%%
# Haversine formula
from math import asin, sqrt, sin, cos, radians

object_lat = 49.82587
object_lon = 23.95795
lat = 49.82403251406
lon = 23.9536850420042


distance = 2 * 6371 * asin(sqrt(sin((radians(lat) - radians(object_lat)) / 2) ** 2 + cos(radians(lat)) * cos(radians(object_lat)) * sin((radians(lon) - radians(object_lon)) / 2) ** 2));

print(distance)



#%%
# work with list
def Convert(tup, di):
    di = dict(tup)
    return di

def Convert_1(tup, di):
    for a, b in tup:
        di.setdefault(a, 1)
    return di

choise_1 = [('Прибудинкова територія','Прибудинкова територія'),('Зелене оточення','Зелене оточення'),('Шум загазованість','Шум загазованість'),('Виробнича зона','Виробнича зона')]
choise_2 = [('Стан будинку відповідає його віку','Стан будинку відповідає його віку'),('Значні тріщини в стінах, сирість, руйнування даху','Значні тріщини в стінах, сирість, руйнування даху'),('Волосяні тріщини, відпадання штукатурки фасаду, протікання даху','Волосяні тріщини, відпадання штукатурки фасаду, протікання даху'),('Стан будинку відповідає його віку','Стан будинку відповідає його віку'),('Проведено капітальний ремонт','Проведено капітальний ремонт'),('Проведено капітальний ремонт - ексклюзив','Проведено капітальний ремонт - ексклюзив')]
choise_3 = [('Стан добрий','Стан добрий'),('Незадовільний','Незадовільний'),('Задовільний','Задовільний'),('Відмінний','Відмінний'),('Ексклюзив','Ексклюзив'),('"Нульовий" цикл','"Нульовий" цикл')]
choise_4 = [('Вхід з балкону','Вхід з балкону'),('Вхід в кухню','Вхід в кухню'),('Кухня без вікна','Кухня без вікна'),('Вигоди в спільному користуванні','Вигоди в спільному користуванні'),('Без вигод','Без вигод')]
choise = choise_1+choise_2+choise_3+choise_4
      
# Driver Code    
dictionary = {}
print (Convert_1(choise, dictionary))

choise_dictionary = {'Прибудинкова територія': 0.95, 'Зелене оточення': 0.95, 'Шум загазованість': 0.95, 'Виробнича зона': 0.95, 'Стан будинку відповідає його віку': 1.0, 'Значні тріщини в стінах, сирість, руйнування даху': 0.75, 'Волосяні тріщини, відпадання штукатурки фасаду, протікання даху': 0.85, 'Проведено капітальний ремонт': 1.15, 'Проведено капітальний ремонт - ексклюзив': 1.25, 'Стан добрий': 1, 'Незадовільний': 1, 'Задовільний': 1, 'Відмінний': 1, 'Ексклюзив': 1, '"Нульовий" цикл': 1, 'Вхід з балкону': 1, 'Вхід в кухню': 1, 'Кухня без вікна': 1, 'Вигоди в спільному користуванні': 1, 'Без вигод': 1}

#%%
# import csv file
import csv, os
records = []
f = open("D:/python/mysite/online/table.csv", encoding='utf-8')
for row in csv.reader(f):
    #for r in row:unicode(cell, 'utf-8')
    records.append(row)
    print(row[2])

f.close()


#%%
# work with MySQL
#pip install mysql-connector-python
import mysql.connector
import sqlite3
import os


#sqlite3
#sqlite3 list tables in base
def sql_fetch(con, sql):
    cursorObj = con.cursor()
    cursorObj.execute(sql)
    print(cursorObj.fetchall())
# drop table
def sql_drop(con):
    cursorObj = con.cursor()
    cursorObj.execute('DROP table if exists rooms_room')
    print(cursorObj.fetchall())
# insert table
def sql_insert(con,title, slug, updated_on, content, created_on, status):
    cursorObj = con.cursor()
    sql = 'INSERT INTO blog_note(title, slug, updated_on, content, created_on, status) VALUES(?,?,?,?,?,?)'
    val = (title, slug, updated_on, content, created_on, status)
    cursorObj.execute(sql, val)
    con.commit()


#sqlite3
base_dir= os.path.dirname(os.path.realpath(__file__))
con = sqlite3.connect(os.path.join(base_dir,'db.sqlite3'))
#con = sqlite3.connect('E:/install/python/project_www/septima_vercel/db.sqlite3')
sql = 'SELECT name from sqlite_master where type= "table"' # name all tables
#sql = ' SELECT ID FROM auth_user'  # table structure
sql_fetch(con, sql)
con.close()

#%%
import pandas as pd
import sqlite3

base_dir= os.path.dirname(os.path.realpath(__file__))
con = sqlite3.connect(os.path.join(base_dir,'db.sqlite3'))
sql = 'SELECT * from cards_cards'

df = pd.read_sql(sql, con)
#df = df[['id', 'name_group', 'coefficient', 'image', 'description', 'status', 'author_id', 'image']]
#df.to_csv('work.csv', index = False, header= True)

print(df)

for item in df[0:1]:
    print(item)
print("------------------")
for item in df.index[0:2]:
    print(df.loc[item])
    #print('---------------------')



con.close()