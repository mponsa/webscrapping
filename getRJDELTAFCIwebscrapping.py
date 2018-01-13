# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 16:07:19 2017

@author: manue
"""
#RJ DELTA fci webscrapping

import requests
from bs4 import BeautifulSoup
import pandas as pd
import re


#Recopilación y manejo de datos desde web---------------------------------------------------------------------------#

url = 'https://deltaasset.com.ar/VFPublic/frwreportes.aspx?rpt=VALORESCPDIARIOS'
r = requests.get(url)
soup = BeautifulSoup(r.content,'html.parser') #Devuelve el html de la página.
date = re.search(r'\d{2}/\d{2}/\d{4}',soup.find('td', class_="TitReporte").text).group()



#TR Linea VCP_row - Linea de tabla con precios FCI. Cada TR VCP_row es un fondo.
#TD Columna TablaVCP_Col1 -> Nombre fondo.
#TD Columna TablaVCP_Col2 -> Clase.
#TD Columna TablaVCP_Col3 -> Moneda.
#TD Columna TABLAVCP_Col4 -> Precio cuotaparte.
#TD Columna TablaVCP_Col5 -> Patrimonio neto del fondo.
#TD Columna TablaVCP_Col6 -> Variación diaria.
#TD Columna TablaVCP_Col7 -> Variación mes anterior.
#TD Columna TablaVCP_Col8 -> Variación año anterior.

names = []
clases = []
currs = []
prices =  []
netvals = []
dayvars = []
lmonthvars = []
lyearvars = []

for col in soup.find_all('tr', class_="TablaVCP_Row"):  
    if(col.find(class_="TablaVCP_Col1") != None):
        name = col.find(class_="TablaVCP_Col1").text
        clase = col.find(class_="TablaVCP_Col2").text
        curr = col.find(class_="TablaVCP_Col3").text
        price = col.find(class_="TablaVCP_Col4").text
        netval = col.find(class_="TablaVCP_Col5").text
        dayvar = col.find(class_="TablaVCP_Col6").text
        lmonthvar = col.find(class_="TablaVCP_Col7").text
        lyearvar = col.find(class_="TablaVCP_Col8").text
    else:#Si no tiene COL1 Es un extend del fondo anterior Solo trae Col2 Col4 Col6 Col7 y Col8.
        clase = col.find(class_="TablaVCP_Col2").text
        price = col.find(class_="TablaVCP_Col4").text
        dayvar = col.find(class_="TablaVCP_Col6").text
        lmonthvar = col.find(class_="TablaVCP_Col7").text
        lyearvar = col.find(class_="TablaVCP_Col8").text
    
    names.append(name)
    clases.append(clase)
    currs.append(curr)
    prices.append(price)
    netvals.append(netval)
    dayvars.append(dayvar)
    lmonthvars.append(lmonthvar)
    lyearvars.append(lyearvar)

for col in soup.find_all('tr', class_="TablaVCP_RowAlt"):  
    if(col.find(class_="TablaVCP_Col1") != None):
        name = col.find(class_="TablaVCP_Col1").text
        clase = col.find(class_="TablaVCP_Col2").text
        curr = col.find(class_="TablaVCP_Col3").text
        price = col.find(class_="TablaVCP_Col4").text
        netval = col.find(class_="TablaVCP_Col5").text
        dayvar = col.find(class_="TablaVCP_Col6").text
        lmonthvar = col.find(class_="TablaVCP_Col7").text
        lyearvar = col.find(class_="TablaVCP_Col8").text
    else:#Si no tiene COL1 Es un extend del fondo anterior Solo trae Col2 Col4 Col6 Col7 y Col8.
        clase = col.find(class_="TablaVCP_Col2").text
        price = col.find(class_="TablaVCP_Col4").text
        dayvar = col.find(class_="TablaVCP_Col6").text
        lmonthvar = col.find(class_="TablaVCP_Col7").text
        lyearvar = col.find(class_="TablaVCP_Col8").text
        
    names.append(name)
    clases.append(clase)
    currs.append(curr)
    prices.append(price)
    netvals.append(netval)
    dayvars.append(dayvar)
    lmonthvars.append(lmonthvar)
    lyearvars.append(lyearvar)
    
    
data = pd.DataFrame({
        "date":date,
        "name":names,
        "clase":clases,
        "price":prices,
        "netval":netvals,
        "dayvar":dayvars,
        "lmonthvar":lmonthvars,
        "lyearvar":lyearvars
        })
data = data[["date","name","clase","price","netval","dayvar","lmonthvar","lyearvar"]]
data = data.sort_values("name")
#-----------------------------------------------------------------------------------------------------------------------#
        
#Formateo de datos------------------------------------------------------------------------------------------------------#
data.to_csv("DatosFCI.csv",mode = 'a')

