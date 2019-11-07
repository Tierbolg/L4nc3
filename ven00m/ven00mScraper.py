# Import Libraries
import csv
import sys
import urllib.request

import requests
from bs4 import BeautifulSoup

import PROPERTIES


def main():
    """Central process"""
    workingwithalbumimages(PROPERTIES.DOWNLOAD_URL)


def workingwithalbumimages(parsingUrl):
    """Return the information for storage therow of each album"""
    datos = urllib.request.urlopen(parsingUrl).read().decode()
    soup = BeautifulSoup(datos)
    tags = soup('img')
    listOfImages = []
    for tag in tags:
        srcToCheck = tag.get('src')
        if not (srcToCheck == None) and ("small" in srcToCheck):
            print(srcToCheck)
            listOfImages.append(PROPERTIES.HTTPS_CONSTANT+srcToCheck)
    str1 = ", "    
    print("final: "+str1.join(listOfImages))
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


def addrowfofile(pathFile, rowToAdd):
    pass


if __name__ == "__main__":
    main()
