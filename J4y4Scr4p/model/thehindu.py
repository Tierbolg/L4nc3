# Import Libraries
import csv
import sys
import urllib.request
import config.properties as properties
from model.postWordpress import postWordpress

import requests
from bs4 import BeautifulSoup
from selenium import webdriver


def extractposts(mapapagina):
    urlgenerada=mapapagina['link']+mapapagina['categoryweb']
    listposts=[]
    print(urlgenerada)
    datos = urllib.request.urlopen(urlgenerada).read()
    soup= BeautifulSoup(datos, "html.parser")
    # Get the list of posts
    bloquedeposts=soup.findAll("div",{"class":"col-sm-12 col-xs-12 tstry-feed-sml-a"})
    for post in range(1,int(mapapagina['articles'])+1):
        postToScrap=bloquedeposts[int(post)]
        imagen=postToScrap.findAll("div",{"class":"stry-hd-sml-t3-img lazy-loaded"})
        print(post)
        fuenteimagen=imagen[0].find('img')['src']
        titulo=postToScrap.find('a')['title']
        urlvisitar=postToScrap.find('a')['href']
        content=postToScrap.findAll("div",{"class":"view_mov_poli_content"})[0].get_text()
        postWordLlenar=postWordpress(fuenteimagen, titulo, urlvisitar, content,mapapagina['categoryWordpress'])        
        listposts.append(postWordLlenar)
    print("Posts extraidos")
    return listposts
