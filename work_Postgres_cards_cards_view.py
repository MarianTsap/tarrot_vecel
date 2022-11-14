# -*- coding: utf-8 -*-
# importing psycopg2 module
import psycopg2
import pandas as pd
import sqlite3
import os



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
# list that contain records to be inserted into table

# inserting record into employee table

cursor.execute("SELECT * FROM cards_cards")
# data = cursor.fetchone() select one records
data = cursor.fetchmany(size=5)
print(data)
print("--------------------------------------")
print("List has been inserted to employee table successfully...")

# Commit your changes in the database
conn.commit()

# Closing the connection
conn.close()


