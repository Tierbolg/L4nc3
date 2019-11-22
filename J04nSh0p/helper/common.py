#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Clase de generacion de Categorias"""

__author__ = "Tierbolg"
__copyright__ = "Curso de Python"
__credits__ = ["Gilberto", "Joan"]
__license__ = "Apache 2.0"
__version__ = "1.0"
__email__ = "tierbolg@outlook.com"
__status__ = "Development"

import config.PROPERTIES as PROPERTIES
import shopify.shopify as helperShopify
import csv
import json
import time
import urllib.request
from urllib.error import HTTPError
from discord_webhook import DiscordWebhook, DiscordEmbed


def get_page(url, page, collection_handle=None):
    full_url = url
    if collection_handle:
        full_url += '/collections/{}'.format(collection_handle)
    full_url += '/products.json'
    req = urllib.request.Request(
        full_url + '?page={}'.format(page),
        data=None,
        headers={
            'User-Agent': PROPERTIES.USER_AGENT
        }
    )
    while True:
        try:
            data = urllib.request.urlopen(req).read()
            break
        except HTTPError:
            print('Blocked! Sleeping...')
            time.sleep(180)
            print('Retrying')

    products = json.loads(data.decode())['products']
    return products


def filtercollection():
    Collection = []
    with open(PROPERTIES.csv_configuration, newline='') as f:
        reader = csv.DictReader(f, delimiter=',', quoting=csv.QUOTE_NONE)
        line_count = 0
        for row in reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            print(
                f'\t{row["Collection"]} with product:  {row["Url"]} ')
            if row["Collection"] not in Collection:
                Collection.append(row["Collection"])
            line_count += 1

    print(f'Processed {line_count} lines.')
    return Collection


def extract_products_collection(url, col):
    page = 1
    products = get_page(url, page, col)
    while products:
        for product in products:
            title = product['title']
            product_type = product['product_type']
            product_url = url + '/products/' + product['handle']
            product_handle = product['handle']

            def get_image(variant_id):
                images = product['images']
                for i in images:
                    k = [str(v) for v in i['variant_ids']]
                    if str(variant_id) in k:
                        return i['src']

                return ''

            for i, variant in enumerate(product['variants']):
                price = variant['price']
                option1_value = variant['option1'] or ''
                option2_value = variant['option2'] or ''
                option3_value = variant['option3'] or ''
                option_value = ' '.join([option1_value, option2_value,
                                         option3_value]).strip()
                sku = variant['sku']
                main_image_src = ''
                if product['images']:
                    main_image_src = product['images'][0]['src']

                image_src = get_image(variant['id']) or main_image_src
                stock = 'Yes'
                if not variant['available']:
                    stock = 'No'

                row = {'sku': sku, 'product_type': product_type,
                       'title': title, 'option_value': option_value,
                       'price': price, 'stock': stock, 'body': str(product['body_html']),
                       'variant_id': product_handle + str(variant['id']),
                       'product_url': product_url, 'image_src': image_src, 'checkout_id': str(variant['id'])}
                for k in row:
                    row[k] = str(row[k].strip()) if row[k] else ''
                yield row

        page += 1
        products = get_page(url, page, col)


def generatecommonfile():
    with open(PROPERTIES.fileTemp, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['Collection', 'Title', 'Price', 'Checkout',
                         'UrlImage', 'Product_Url',
                         'Checkout_Url', 'Size','Stock'])

        for collection in filtercollection():
            collectionName = ""
            title = ""
            price = ""
            checkout = ""
            urlImage = ""
            product_url = ""
            checkout_url = ""
            size = ""
            stock=""
            dictsizeCheck = {}
            for product in extract_products_collection(PROPERTIES.url, collection):
                collectionName = collection
                title = product['title']
                price = product['price']
                checkout_id = product['checkout_id']
                size = product['option_value']
                urlImage = product['image_src']
                product_url = product['product_url']
                checkout_url = PROPERTIES.checkout_url+checkout_id+PROPERTIES.checkout_quantity
                #dictsizeCheck[size] = checkout_url
                stock=product['stock']
                # print("Title: {} Price: {} checkout: {} size: {} ".format(
                #    title, price, checkout_url, size))
                
                writer.writerow([
                    collectionName, title, price, checkout_id, urlImage, product_url, checkout_url, size,stock])


def discordsend(title, product_url, urlImage, checkout_url, price, size, dictsizeCheck):
    webhook = DiscordWebhook(url=PROPERTIES.url_webhook, username="Admin")
    embed = DiscordEmbed(title="**"+title+"**", description='', color=6225906)
    embed.set_footer(
        text='Cop Hype', icon_url="https://cdn.discordapp.com/attachments/62788690058805252/629012787569492008/background.png")
    embed.set_timestamp()
    embed.set_thumbnail(url=urlImage)
    embed.set_url(product_url)
    embed.add_embed_field(name='Kith', value='Restock', inline=True)
    #embed.add_embed_field(name='Checkout', value="**PAYPAL**", color=6225906, inline=True)
    embed.add_embed_field(name='Price', value="€"+str(price), inline=False)
    valueImage = ""

    for x, y in dictsizeCheck.items():
        #print(x, y)
        valueImage = valueImage+"**"+'['+x+']'+'('+y+')'+"**"+"\n"

    embed.add_embed_field(name='Size', value=valueImage, inline=False)
    webhook.add_embed(embed)
    webhook.execute()


def getproductoslist(coleccionRevisar):
    productosdeexcel = []
    with open(PROPERTIES.csv_configuration, newline='') as f:
        reader = csv.DictReader(f, delimiter=',', quoting=csv.QUOTE_NONE)
        line_count = 0
        for row in reader:
            if row["Collection"] in coleccionRevisar:
                productosdeexcel.append(row["Url"])
            line_count += 1
    return productosdeexcel


def llenadictproductos():
    dictCache = {}
    # Lista de colecciones diferentes
    listacolleccionesfiltradas = filtercollection()
    for collection1 in filtercollection():
        dictCache[collection1] = extract_products_collection(
            PROPERTIES.url, collection1)
    return dictCache


def buscarproductos():
    with open(PROPERTIES.csv_configuration, newline='') as f:
        reader = csv.DictReader(f, delimiter=',', quoting=csv.QUOTE_NONE)
        for row in reader:
            title = ""
            price = ""
            urlImage = ""
            product_url = ""
            checkout_url = ""
            size = ""
            dictsizeCheck = {}
            # Cada renglon es un producto, muchas tallas
            claseGenerada = comparador(row['Url'], row['Collection'])
            print(claseGenerada.title)
            discordsend(claseGenerada.title, claseGenerada.product_url, claseGenerada.urlImage,
                        claseGenerada.checkout_url, claseGenerada.price, claseGenerada.size, claseGenerada.dictsizeCheck)
            print(row)


class Envios:
    title = ''
    price = ''
    product_url = ''
    checkout = ''
    size = ''
    urlImage = ''
    checkout_url = ''
    dictsizeCheck = {}
    pass


def comparador(urlCompare, coleccioncheck):
    envio = Envios()
    dictsizeCheck = {}
    for product in extract_products_collection(PROPERTIES.url, coleccioncheck):
        # print(product['product_url'])
        if product['stock'] == "Yes" and urlCompare == product['product_url']:
            envio.title = product['title']
            envio.price = product['price']
            envio.checkout = product['checkout_id']
            size = product['option_value']
            envio.urlImage = product['image_src']
            checkout_id = product['checkout_id']
            envio.product_url = product['product_url']
            checkout_url = PROPERTIES.checkout_url+checkout_id+PROPERTIES.checkout_quantity
            dictsizeCheck[size] = checkout_url
            envio.dictsizeCheck = dictsizeCheck
    return envio


def buscarproductos2():
    with open(PROPERTIES.csv_configuration, newline='') as f:
        reader = csv.DictReader(f, delimiter=',', quoting=csv.QUOTE_NONE)
        for row in reader:
            title = ""
            price = ""
            urlImage = ""
            product_url = ""
            checkout_url = ""
            size = ""
            dictsizeCheck = {}
            # Cada renglon es un producto, muchas tallas
            claseGenerada = comparador2(row['Url'], row['Collection'])
            print(claseGenerada.title)
            discordsend(claseGenerada.title, claseGenerada.product_url, claseGenerada.urlImage,
                        claseGenerada.checkout_url, claseGenerada.price, claseGenerada.size, claseGenerada.dictsizeCheck)
            print(row)


def comparador2(urlCompare, coleccioncheck):
    envio = Envios()
    dictsizeCheck = {}
    with open(PROPERTIES.fileTemp) as resultadoProductos:
        csvReader = csv.reader(resultadoProductos, delimiter=',')
        for row in csvReader:
            # Compare product with collection
            if coleccioncheck.lower() == row[0].lower() and urlCompare == row[5] and row[8] == "Yes":
                envio.title = row[1]
                envio.price = row[2]                
                size = row[7]
                envio.size=size
                envio.urlImage = row[4]
                envio.product_url = row[5]
                envio.checkout_url = row[6]
                dictsizeCheck[size] = row[6]
                envio.dictsizeCheck = dictsizeCheck
    return envio
