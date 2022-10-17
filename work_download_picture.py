# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 11:17:29 2022

@author: 1
"""

import requests
import re
import csv
import os
import json
from bs4 import BeautifulSoup
from urllib.parse import urlparse #urllib is a package that collects several modules for working with URLs



def is_digit(str):
    try:
        float(str)
        return True
    except ValueError:
        return False
    
def download(url_,file_name):
    url =url_
    #headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
    r=requests.get(url,timeout=0.5)
    if r.status_code == 200:
        with open(file_name, 'wb') as f:
            f.write(r.content)


def save_list(new_list):
    global dir
    file_xls=dir+'pursing.xlsx'
    import xlsxwriter
    with xlsxwriter.Workbook(file_xls) as workbook:
        worksheet = workbook.add_worksheet()
        for row_num, data in enumerate(new_list):
            worksheet.write_row(row_num, 0, data)

#URL = "https://www.olx.ua/d/uk/obyavlenie/prodazh-orenda-primschen-vd-zabudovnika-novobudov-b-hmelnitskogo-76-IDDUfTt.html#508bc9c987;promoted"
#r = requests.get(URL)

array_pursing=[]
array_pursing_all=[]

dir='e:/install/python/pursing/files/'


for filename in os.listdir(dir):
    file_extension = os.path.splitext(filename)
    if file_extension[1]=='.html' or file_extension[1]=='.htm':
        #print(file_extension[1])
        file=dir+filename
        with open(file, "r", encoding='utf-8') as f:
            count=0
            text= f.read()
            f.close()
            soup = BeautifulSoup(text, 'html.parser')
            #print(soup)       
            # -----------------------OLX pursing-----------------------
            
            print(count,'-------------------')
            

            
            #img
            img_array=[]
            tags = soup.find('body')
            tags = tags.find_all(href=re.compile("jpg"))
            
            for it in tags:
                count=count+1
                url='https://www.sacred-texts.com/tarot/pkt/'+it.get('href')
                if len(tags)>1:
                    file_name=dir+filename.split('.')[0]+'_'+str(count)+'.jpg'
                else:
                    file_name=dir+filename.split('.')[0]+'.jpg'
                print(url)
                download(url,file_name)
            
            
            
            
            '''
            for script
            img_array=[]
            tags = soup.find_all('script',type="application/ld+json")
            print(tags)
            #img_dic=dict(x.split(":") for x in tag.get_text().split(","))
            for tag in tags:
                description=re.sub('[{}"\n +]', "",tag.get_text())
                img_array=(description.split(","))
                for it in img_array:
                    if 'image:' in it:
                        count=count+1
                        print(re.sub('image:', "",it))
                        url=re.sub('image:', "",it)
                        file_name=dir+filename.split('.')[0]+'_'+str(count)+'.jpg'
                        print(file_name)
                        download(url,file_name)
            '''


'''
            array_pursing=[array_location[1],array_location[2],array_location[3],array_area['Загальна площа'],array_area['Площа ділянки'],value_float,description,url]
            array_pursing_all.append(array_pursing)
#array_pursing=[array_location[0],array_location[1],array_location[2]]
#print(array_pursing_all)
save_list(array_pursing_all)
'''
        
