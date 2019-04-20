from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import json
from bs4 import BeautifulSoup
from pandas import DataFrame
import pandas as pd
import csv
import sys
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-setuid-sandbox")
chrome_options.binary_location = r"C:\Users\abc\AppData\Local\Google\Chrome SxS\Application\chrome.exe"
browser = webdriver.Chrome(chrome_options=chrome_options,executable_path=r"C:\Users\abc\Downloads\chromedriver_win32 (4)\chromedriver",)
n=1
list_data=[]
while n<=22:
    url=' https://www.sothebysrealty.com/eng/associates/usa/'+str(n)+'-pg'
    browser.get(url)
    soup=BeautifulSoup(browser.page_source, 'html.parser')
    get_data1=[]
    get_data=soup.findAll('span', {"class": "agent-item__name"})

    try:
        data_json={}
        for data in get_data:
            data_json['name::']=data.get_text()

            get_data1.append(data.get_text())

    except:
        data_json['name']=''
        lst2=[]
    address=soup.findAll('div', {"class": "street-address"})

    try:
        for data in address:
            data_json['addr ess::']=data.get_text()

            lst2.append(data.get_text())

    except:
        data_json['address']=''

    lst3=[]
    address2=soup.findAll('span', {"class": "address"})

    try:
        for data in address:
            data_json['address2::']=data.get_text()

            lst3.append(data.get_text())

    except:
        data_json['address2']=''

    lst9=[]
    office_name=soup.findAll('span', {"itemprop": "legalName"})

    try:
        for data in office_name:

            data_json['office_name::']=data.text
            lst9.append(data.text)

    except:
        data_json['office_name']=''



    lst4=[]
    city=soup.findAll('span', {"class": "locality"})

    try:
        for data in city:
            data_json['city::']=data.get_text()

            lst4.append(data.get_text())
    except:
        data_json['city']=''
    lst5=[]
    state=soup.findAll('span', {"class": "region"})
    # print(state)
    try:
        for data in state:
            data_json['state::']=data.get_text()

            lst5.append(data.get_text())
    except:
        data_json['state']=''
    lst6=[]
    zip=soup.findAll('span', {"class": "postal-code"})

    try:
        for data in zip:
            data_json['get_zip::']=data.get_text()
            lst6.append(data.get_text())
    except:
        data_json['get_zip']=''

    lst7=[]
    lst8=[]

    phone1=soup.findAll('a', {"class": "o-phone"})
    for data in phone1:

        try:
            if '+' in data.get('href').replace('tel:',''):

                data_json['get_phone::'] = data.get('href').replace('tel:','')

                lst7.append(data.get('href').replace('tel:',''))

            else:

                data_json['get_phone::'] = data.get('href').replace('tel:', '')
                lst8.append(data.get('href').replace('tel:', ''))

        except:
            data_json['get_phone']=''

    data = DataFrame({'Phone-1': lst7})
    data = DataFrame({'state': lst5})
    data1=DataFrame({'city': lst4})
    data2=DataFrame({'officename': lst9})
    name_data=DataFrame({'name': get_data1})


    data5=DataFrame({'Phone-2': lst8})

    getfile=open("phone_getdata.csv",'a+')
    data_=getfile.write(str(data))
    getfile = open("phonedata2.csv", 'a+')
    data = getfile.write(str(data5))
    getfile = open("officename.csv", 'a+')
    data = getfile.write(str(data2))

    getfile = open("city.csv", 'a+')
    data = getfile.write(str(data1))
    getfile = open("name.csv", 'a+')
    data = getfile.write(str(name_data))

    getfile = open("state.csv", 'a+')
    data = getfile.write(str(data))




    n += 1

