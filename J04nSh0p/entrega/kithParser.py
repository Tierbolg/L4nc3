import PROPERTIES
import common
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
    print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
    ahora=datetime.now()
    #helperCommon.buscarproductos()-->pocos productos, algo lento va uno por uno, consume uno por llamada
    #Primero traer archivo de coleccion
    collections = []
    collections = PROPERTIES.collectionToParse.split(',')
    #if os.path.exists(PROPERTIES.fileTemp):
    #    os.remove(PROPERTIES.fileTemp)
    # comentado por eficiencia helperCommon.generatecommonfile()
    print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
    despues=datetime.now()
    diferencia=despues-ahora
    print('Diferencia en segundos: '+str(diferencia.seconds))
    print('Buscando en archivos: '+strftime("%Y-%m-%d %H:%M:%S", gmtime()))
    ahora2=datetime.now()
    common.buscarproductos2()
    print('Buscando en archivos terminado: '+strftime("%Y-%m-%d %H:%M:%S", gmtime()))
    despues2=datetime.now()
    diferencia=despues2-ahora2
    print('Diferencia en segundos: '+str(diferencia.seconds))