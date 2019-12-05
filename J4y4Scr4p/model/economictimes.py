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
    urlgenerada = mapapagina['link']+mapapagina['categoryweb']
    req = urllib.request.Request(
        urlgenerada,
        data=None,
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        }
    )
    listposts = []
    print(urlgenerada)
    datos = urllib.request.urlopen(req).read()
    soup = BeautifulSoup(datos, "html.parser")
    # Get the list of posts
    bloquedeposts = soup.findAll("div", {"class": "eachStory"})
    for post in range(1, int(mapapagina['articles'])+1):
        postToScrap = bloquedeposts[int(post)]
        print(post)
        fuenteimagen = postToScrap.find('img')['data-original']
        content = postToScrap.find('p').get_text()
        titulo = postToScrap.find('img')['alt']
        videocheck = postToScrap.find('a')['href']
        if videocheck[0] == '/':
            videocheck = videocheck[1:]
        urlvisitar = mapapagina['link'] + videocheck
        postWordLlenar = postWordpress(
            fuenteimagen, titulo, urlvisitar, content, mapapagina['categoryWordpress'])
        listposts.append(postWordLlenar)
    print("Posts extraidos")
    return listposts
