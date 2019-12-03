# Import Libraries
import csv
import sys
import urllib.request
import config.properties as properties

import requests
from bs4 import BeautifulSoup
from selenium import webdriver

def extractposts(mapapagina):
    urlgenerada=mapapagina['link']+mapapagina['categoryweb']
    print(urlgenerada)
    datos = urllib.request.urlopen(urlgenerada).read()
    soup= BeautifulSoup(datos, "html.parser")
    # Get the list of posts
    bloquedeposts=soup.findAll("div",{"class":"movies_news_description_container float-left"})
    for post in range(1,int(mapapagina['articles'])):
        postToScrap=bloquedeposts[int(post)]
        imagen=postToScrap.findAll("div",{"class":"img_plc"})
        print(post)
        fuenteimagen=imagen[0].find('img')['src']
        titulo=postToScrap.find('a')['title']
        urlvisitar=postToScrap.find('a')['href']
        content=postToScrap.findAll("div",{"class":"view_mov_poli_content"})[0].get_text()

        for tag in imagen:
            srcToCheck = tag.get('src')
            print (srcToCheck)
    #albumName = soup.findAll("span", {"class": "showalbumheader__gallerytitle"})[
    #    0].get_text()
    # Get the description of the album
    #albumDescription = soup.findAll(
    #    "div", {"class": "movies_news_description_container float-left"})[0].get_text()
    #print("The name of the album is: "+albumName)

    # Get common object to parse the html
    driver = webdriver.Firefox(executable_path=properties.PATH_SELENIUM)
    driver.get(urlgenerada)    
    htmlObtenido = driver.page_source
    soup1 = BeautifulSoup(htmlObtenido)
    bloquedeposts1=soup1.findAll("div",{"class":"movies_news_description_container float-left"})
    for post in mapapagina['articles']:
        postToScrap=bloquedeposts[int(post)]
        imagen=postToScrap.findAll("div",{"class":"img_plc"})
        fuenteimagen=imagen[0].find('img')['src']
        titulo=postToScrap.find('a')['title']
        urlvisitar=postToScrap.find('a')['href']
        content=postToScrap.findAll("div",{"class":"view_mov_poli_content"})

