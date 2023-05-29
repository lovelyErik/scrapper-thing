import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

startUrl="https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
browser=webdriver.Chrome("C:/Users/Lap_AcerTM/Documents/scrapping/chromedriver.exe")
browser.get(startUrl)
planet_data=[]
def scrape():
    for i in range(0,10):
        print(f"scrapping page {i+1}...")
        soup=BeautifulSoup(browser.page_source,"html.parser")
        for ul_tag in soup.find_all("ul",attrs={"class","exoplanet"}):
            li_tags=ul_tag.find_all("li")
            temp_list=[]
            for index,li_tag in enumerate(li_tags):
                if index==0:
                    temp_list.append(li_tag.find_all("0")[0].contents[0])
                else:
                    try: 
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")
        planet_data.append(temp_list)
    print(planet_data[1])