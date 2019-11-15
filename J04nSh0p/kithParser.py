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

if __name__ == '__main__':

    # con esto toma todas las colecciones de la página
    collections = []
    # Extract global collections and show in terminal
    #for col in helperShopify.get_page_collections(PROPERTIES.url):
        # Complete json print(col)
    #    print(col['handle'])
    #    collections.append(col['handle'])

    # listaAdidas=helperShopify.extract_products_collection(PROPERTIES.url,"yeezy-adidas")
    # for product in listaAdidas:
    #    print('hola')
    # print('adios')

    # Generar archivos por categoria
    helperCommon.generatecommonfile()


# Buscar producto en categoria descargada
# Guardar si el producto ya está disponible

# ¿Que pasa si descargo la categoria, producto esta, mando alerta, guardo que ya mandeo sigo enviando alerta?
