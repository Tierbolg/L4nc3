import config.PROPERTIES as PROPERTIES
import shopify.shopify as helperShopify
import helper.common as helperCommon
import sys
import csv
import json
import time
import urllib.request
from urllib.error import HTTPError
from optparse import OptionParser
from time import gmtime, strftime 
import os

from datetime import datetime, date, time, timedelta
import calendar

if __name__ == '__main__':

    # con esto toma todas las colecciones de la página
    collections = []
    # Extract global collections and show in terminal
    #for col in helperShopify.get_page_collections(PROPERTIES.url):
    #    print(col)
    #    print(col['handle'])
    #    collections.append(col['handle'])

    # listaAdidas=helperShopify.extract_products_collection(PROPERTIES.url,"yeezy-adidas")
    # for product in listaAdidas:
    #    print('hola')
    # print('adios')

    #mapacoletzione=helperCommon.llenadictproductos()
    print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
    ahora=datetime.now()
    #helperCommon.buscarproductos()
    #Primero traer archivo de coleccion
    collections = []
    collections = PROPERTIES.collectionToParse.split(',')
    if os.path.exists(PROPERTIES.fileTemp):
        os.remove(PROPERTIES.fileTemp)

    # Archivo sin el checkout
    # helperShopify.extract_products(PROPERTIES.url,PROPERTIES.fileTemp,collections)
    helperCommon.generatecommonfile()
    print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
    despues=datetime.now()
    diferencia=despues-ahora
    print('Diferencia en segundos: '+str(diferencia.seconds))
    print('Buscando en archivos: '+strftime("%Y-%m-%d %H:%M:%S", gmtime()))
    ahora2=datetime.now()
    helperCommon.buscarproductos2()
    print('Buscando en archivos terminado: '+strftime("%Y-%m-%d %H:%M:%S", gmtime()))
    despues2=datetime.now()
    diferencia=despues2-ahora2
    print('Diferencia en segundos: '+str(diferencia.seconds))

#Si lo hago eficiente
#generar csv de las colecciones
#iterar sobre los archivos, no ir de nuevo a conectarme