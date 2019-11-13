from selenium import webdr
from selenium.webdriver.common.desired_capabilities import DesirCapabilities
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.keys import Keys
import sys
import random
from selenium.webdriver.chrome.options import Options
from discord_webhook import DiscordWebhook, DiscordEmbed



urls =[ 
    
    "https://www.sivasdescalzo.com/en/adidas-yeezy-desert-boot-fv5677",
    "https://www.sivasdescalzo.com/fr/jordan-mars-270-cd7070-135",
    "https://www.sivasdescalzo.com/fr/jordan-wmns-air-7-retro-313358-006",
    "https://www.sivasdescalzo.com/fr/jordan-spizike-315371-051"
]






user_agent_list = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/44.0.2403.155 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36',
    'Mozilla/5.0 (X11; Linux i686; rv:64.0) Gecko/20100101 Firefox/64.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:64.0) Gecko/20100101 Firefox/64.0',
    'Mozilla/5.0 (X11; Linux i586; rv:63.0) Gecko/20100101 Firefox/63.0',
    'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:63.0) Gecko/20100101 Firefox/63.0',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.10; rv:62.0) Gecko/20100101 Firefox/62.0',
    'Opera/9.80 (Windows NT 6.1; WOW64) Presto/2.12.388 Version/12.18',
    'Opera/9.80 (Linux armv7l) Presto/2.12.407 Version/12.51 , D50u-D1-UHD/V1.5.16-UHD (Vizio, D50u-D1, Wireless)',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36 OPR/56.0.3051.52',
    'Opera/9.80 (Windows NT 5.1; U; ru) Presto/2.9.168 Version/11.50',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36 OPR/34.0.2036.25',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36 OPR/52.0.2871.99',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36 OPR/33.0.1990.115',
    'Opera/9.80 (Windows NT 6.2; Win64; x64) Presto/2.12.388 Version/12.16',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36 OPR/53.0.2907.99',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
    'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0'
	]



def getinfo(url):
    user_agent = random.choice(user_agent_list)
    opts = Options()
    opts.add_argument("user-agent="+user_agent)
    opts.add_argument("--headless")
    browser=webdriver.Chrome(options=opts)
    #browser.maximize_window()
    print("Scraping :" + url)
    browser.get(url)

    price=browser.find_element_by_xpath('//*[@id="product_addtocart_form"]/div[3]/div/div[1]/span/b').get_attribute("innerHTML")

    picture = browser.find_element_by_xpath('//img[@class="lazyOwl cloudzoom"]').get_attribute('src')

    title = browser.find_element_by_xpath('//h1[@class="product-data-title"]/span[2]').get_attribute("innerHTML")
    
    formAction = browser.find_element_by_xpath('//form[@class="custom"]').get_attribute("action")

    form_key = browser.find_element_by_xpath('//input[@name="form_key"]').get_attribute("value")

    referer = browser.find_element_by_xpath('//input[@name="referer"]').get_attribute("value")

    product = browser.find_element_by_xpath('//input[@name="product"]').get_attribute("value")
    
    
    sizes = browser.find_elements_by_xpath('//div[@class="content size-options size_eu-options"]/ul/li/a') 
    

    
    # print("Title = " + title)
    # print("Price = " + price)
    # print(picture)
    
    sizeTup = list()
    for size in sizes :
        
        sizeTup.append( [ size.get_attribute("data-optionindex") , size.get_attribute("innerHTML") ] )
    
    text = str()

    i=0
    for size in sizeTup :
        if (i > 7):
            break
        i+=1

        if (size[0] != '0'):
            link = "https://cophype.com/svd/?id={}&sds={}".format(size[0],product)
            #link = "https://cophype.com/p/?id="
            text += "{} [**[ATC]**]({}) \n".format(size[1] , link)
    #print("Text =\n"+text)
    sizeText = str()
    for size in sizeTup :
        sizeText += " "  + size[1]

    filename = "sizes/"+str(product)+".sz"

    try:
        file1 = open(filename,"r+")
        LastSizes = file1.read()
        file1.close()
    except :
        LastSizes=""
    
    if (LastSizes != sizeText):
        isSend = True
    else :
        isSend = False
    
    


    fileWriter =  open(filename,"w")
    fileWriter.write(sizeText)
    fileWriter.close()

    if (isSend):
        embed = DiscordEmbed(title="**"+title+"**", description='', color=6225906)
        
        embed.set_footer(text='Cop Hype',icon_url="https://cdn.discordapp.com/attachments/62788690058805252/629012787569492008/background.png")
        embed.set_timestamp()
        embed.set_thumbnail(url=picture)
        embed.set_url(url)
        embed.add_embed_field(name='Sivasdescalzo - SVD', value='Restock' ,inline = True)
        embed.add_embed_field(name='Checkout', value='[**[PAYPAL]**](https://www.sivasdescalzo.com/en/checkout/)' ,inline = True)
        embed.add_embed_field(name='Price', value=str(price)+"€",inline = False)
        embed.add_embed_field(name='Size', value=str(text),inline = False)
        webhook.add_embed(embed)
        webhook.execute()

    browser.close()
    print("Done!")


webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/272097700085801/W02I49OYVj84j_Chn_jTiOwczaShSeIYbJ2_lp4h9XY6gNXBOWiQ8m4P5DbZNJ9YTnbY', username="SVD")


while True:
    for url in urls :
        try:
            getinfo(url)
        except :
            print("Error maybe next time!")
            break
            #continue