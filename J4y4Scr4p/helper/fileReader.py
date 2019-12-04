import config.properties as properties
import csv
import helper.scraper as scraper
import model.greatandhra as greatandhraclass

def abrearchivocsvconfig():
    with open(properties.CSV_CONFIGURATION_FILE, newline='') as f:
        reader = csv.DictReader(f, delimiter=',', quoting=csv.QUOTE_NONE)
        for row in reader:            
            print(row)
            if(row['class']=='greatandhra'):
                return greatandhraclass.extractposts(row)
