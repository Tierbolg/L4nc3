import config.properties as properties
import helper.wordpress as wordpress
import helper.fileReader as fileReader
import sys
import urllib.request
import csv
import model.greatandhra as greatandhraclass
import model.thehindu as thehinduclass
import model.deccanchronicle as deccanchronicleclass
import model.newindianexpress as newindianexpressclass
import model.economictimes as economictimesclass
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

def main():
    with open(properties.CSV_CONFIGURATION_FILE, newline='') as f:
        reader = csv.DictReader(f, delimiter=',', quoting=csv.QUOTE_NONE)
        for row in reader:            
            print(row)
            if(row['class']=='greatandhra'):
                wordpress.publicarlistadeposts(greatandhraclass.extractposts(row))
            if(row['class']=='thehindu'):
                wordpress.publicarlistadeposts(thehinduclass.extractposts(row))
            if(row['class']=='deccanchronicle'):
                wordpress.publicarlistadeposts(deccanchronicleclass.extractposts(row))
            if(row['class']=='newindianexpress'):
                wordpress.publicarlistadeposts(newindianexpressclass.extractposts(row))
            if(row['class']=='economictimes'):
                wordpress.publicarlistadeposts(economictimesclass.extractposts(row))
                 

    #print("Lista generada")
    #wordpress.publicarlistadeposts(listaDePosts)
    #entrada default wordpress.publishPost()

if __name__ == "__main__":
    main()