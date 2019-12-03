import config.properties as properties
import helper.wordpress as wordpress
import helper.fileReader as fileReader
import sys
import urllib.request

import requests
from bs4 import BeautifulSoup
from selenium import webdriver

def main():
    fileReader.abrearchivocsvconfig()
    #entrada default wordpress.publishPost()

if __name__ == "__main__":
    main()