# Import Libraries
import csv
import sys
import urllib.request

import requests
from bs4 import BeautifulSoup
from selenium import webdriver

import PROPERTIES


def obtainparsefromhtml(parsingUrl):
    """Return the information of html parsed"""
    datos = urllib.request.urlopen(parsingUrl).read().decode()
    return BeautifulSoup(datos, "lxml")


def getdictionarybyalbum(urlOfAlbum):
    # Get common object to parse the html
    soup = obtainparsefromhtml(urlOfAlbum)
    # Get the name of the album
    albumName = soup.findAll("span", {"class": "showalbumheader__gallerytitle"})[
        0].get_text()
    # Get the description of the album
    albumDescription = soup.findAll(
        "div", {"class": "showalbumheader__gallerysubtitle"})[0].get_text()
    print("The name of the album is: "+albumName)
    print("The description of the album is: "+albumDescription)
    # Get the list of images by album
    listImagesFiltered = workingwithalbumimages(soup)
    print("List of images by album: "+listImagesFiltered)
    # Construct the row for album
    dictForFile = {
        "name": albumName,        
        "description": albumDescription,
        "images": listImagesFiltered,
        "referenceAlbum": urlOfAlbum
    }
    return dictForFile


def main():
    """Central process"""
    if PROPERTIES.CHECK_ONLY_ALBUM:
        # Scrap only one album
        dictForFile = getdictionarybyalbum(PROPERTIES.DOWNLOAD_ALBUM_URL)
        dictFinal = []
        dictFinal.append(dictForFile)
        writefilefromscratch(PROPERTIES.CSV_PATH_FILE, dictFinal)
    else:
        # Get common object to parse the html
        driver = webdriver.Firefox(executable_path=PROPERTIES.PATH_SELENIUM)
        driver.get(PROPERTIES.DOWNLOAD_COMPLETE_ALBUMS)
        htmlObtenido = driver.page_source
        soup1 = BeautifulSoup(htmlObtenido)
        albumsClasses = soup1.find_all("a", class_="album__main album4__main")
        # Result of final dictionary
        dictFinal = []
        for tag1 in albumsClasses:
            referenceAlbum = tag1.get('href')
            if 'album' in referenceAlbum:
                print(referenceAlbum)
                # Get the info of the album
                dictForFile = getdictionarybyalbum(referenceAlbum)
                dictFinal.append(dictForFile)
        writefilefromscratch(PROPERTIES.CSV_PATH_FILE, dictFinal)
        driver.close()


def workingwithalbumimages(soupObtained):
    """Return the information for storage therow of each album"""
    tags = soupObtained('img')
    listOfImages = []
    for tag in tags:
        srcToCheck = tag.get('src')
        if not (srcToCheck == None) and ("small" in srcToCheck):
            # print(srcToCheck)
            listOfImages.append(PROPERTIES.HTTPS_CONSTANT+srcToCheck)
    str1 = ", "
    #print("final: "+str1.join(listOfImages))
    return str1.join(listOfImages)


def writefilefromscratch(pathFile, dictionaryOfAlbums):
    """
    Process to store the information in a csv file
    """
    with open(pathFile, mode='w', newline='') as exitFile:
        fieldnames = ['name', 'description',
                      'images', 'referenceAlbum']
        writer = csv.DictWriter(exitFile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(dictionaryOfAlbums)
        # resultWriter = csv.writer(
        #    exitFile, delimiter=',', quoting=csv.QUOTE_NONE)
        # Write header
        #resultWriter.writerow(['Name', 'Price', 'Description', 'Images'])


if __name__ == "__main__":
    main()
