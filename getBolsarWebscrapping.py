# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 21:36:05 2017

@author: manue
"""

#BOLSAR web scrapping






import requests
url = 'https://www.bolsar.com/VistasDL/PaginaLideres.aspx/GetDataPack'
json_par = {"aEstadoTabla":[{"TablaNombre":"tbAcciones","FiltroVto":"48","FiltroEspecies":"","Orden":"","EsOrdenAsc":True,"FilasxPagina":-1,"MensajeNro":0,"HashCode":0},{"TablaNombre":"tbMontos","FiltroVto":"","FiltroEspecies":"","PagActualNro":"1","Orden":"","EsOrdenAsc":True,"FilasxPagina":-1,"MensajeNro":0,"HashCode":0},{"TablaNombre":"tbIndices","FiltroVto":"","FiltroEspecies":"","PagActualNro":"1","Orden":"","EsOrdenAsc":True,"FilasxPagina":-1,"MensajeNro":0,"HashCode":0}]}
r = requests.post(url, json = json_par )

# =============================================================================
# #JSON DEVUELVE 
# Lista tamaño 3( Accedo al elemento 0 )
# Diccionario (Accedo al elemento aTabla)
# Lista tamaño 27 diccionarios, accedo uno por uno, y obtengo simbolo y ult.precio
# How to access --> json['d'][0]['aTabla'][0...27]['Simbolo']
# =============================================================================
j = r.json()

import json
import pandas as pd
import datetime as dt
import os
import csv

dataset = pd.DataFrame(columns = ['Fecha cotiz','Hora Cotiz','Ticker','Ult.Precio'])

for dic in j['d'][0]['aTabla']:
    dataset.loc[len(dataset)] = [dt.date.today(),dic['HoraCotizacion'],dic['Simbolo'],dic['PrecioUltimo']]


if os.path.exists('LastPrice.csv'):
    dataset.to_csv('LastPrice.csv',mode='a',header=False)
else:
    dataset.to_csv('LastPrice.csv')
    



    
    

    
    


