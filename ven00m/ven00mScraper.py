# Import Libraries
import csv
import sys
import urllib.request

import requests
from bs4 import BeautifulSoup

import PROPERTIES


def obtainparsefromhtml(parsingUrl):
    """Return the information of html parsed"""
    datos = urllib.request.urlopen(parsingUrl).read().decode()
    return BeautifulSoup(datos)


def main():
    """Central process"""
    # Get common object to parse the html
    soup = obtainparsefromhtml(PROPERTIES.DOWNLOAD_URL)
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


def writefilefromscratch(pathFile):
    """
    Process to store the information in a csv file
    """
    with open(pathFile, mode='w') as exitFile:
        resultWriter = csv.writer(
            exitFile, delimiter=',', quoting=csv.QUOTE_ALL)
        # Write header
        resultWriter.writerow(['Name', 'Price', 'Description', 'Images'])


if __name__ == "__main__":
    main()
