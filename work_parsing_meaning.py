# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 11:17:29 2022

@author: 1
"""

#import requests
import re
import csv
import os
from bs4 import BeautifulSoup


def is_digit(str):
    try:
        float(str)
        return True
    except ValueError:
        return False
    
def del_space_array(my_array):
    try:
        for i in range(0,len(my_array)):
            my_array[i]=my_array[i].strip()
            my_array[i]=re.sub(r"\s+", " ", my_array[i])
            
        return my_array
    except ValueError:
        return False

def save_list_csv(array):
    with open("pursing.csv", mode="w", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")
        #for row in array:
        file_writer.writerow(array)
    w_file.close()

def save_list(new_list):
    global dir
    file_xls = os.path.join(dir,'pursing.xlsx')
    import xlsxwriter
    with xlsxwriter.Workbook(file_xls) as workbook:
        worksheet = workbook.add_worksheet()
        for row_num, data in enumerate(new_list):
            worksheet.write_row(row_num, 0, data)

#URL = "https://www.olx.ua/d/uk/obyavlenie/prodazh-orenda-primschen-vd-zabudovnika-novobudov-b-hmelnitskogo-76-IDDUfTt.html#508bc9c987;promoted"
#r = requests.get(URL)

dict_pursing={}
#base_dir = os.path.dirname(os.path.realpath(__file__))
#dir = os.path.join(base_dir,'files')
directory = 'e:/install/python/pursing/files/'
count = 0
for filename in os.listdir(directory):
    file_extension = os.path.splitext(filename)
    if file_extension[1]=='.htm':
        file = os.path.join(directory,filename)
        with open(file, "r") as f: #encoding='utf-8'
            text= f.read()
            f.close()
            soup = BeautifulSoup(text, 'html.parser')
            tag = soup.find('body')
            urls = tag.find_all("p")

            for url in urls[0:-1:1]:
                if "Meanings" in url.get_text():
                    count = count+1
                    x = url.get_text().find("Meanings")
                    #print(filename," - " ,url.get_text()[x:])
                    filename = file_extension[0]+'.jpg'
                    dict_pursing[filename] = url.get_text()[x:]
print(dict_pursing)
            
     
        
