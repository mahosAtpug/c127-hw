from bs4.dammit import encoding_res
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

START_URL = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
browser = webdriver.Chrome("/Users/Soham Gupta/Desktop/C-127/chromedriver_win32")
browser.get(START_URL)
time.sleep(10)

def scrape():
    headers = ["NAME" , "DISTANCE" , 	"MASS" , "RADIUS"]
    planet_data = []
    for i in range(0 , 458): 
        soup = BeautifulSoup(browser.page_source , "html.parser")
        for ul_tag in soup.find_all("ul" , attrs={"class" , "stars"}):
            li_tags = ul_tag.find_all("li")
            temp_list = []
            # iterate over the li tags found in 15 line

            for index , li_tag in enumerate(li_tags):
                if index== 0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")

            planet_data.append(temp_list)
    browser.find_element_by_xpath('//*[@id="mw-content-text"]/div[1]/table/tbody/tr[1]/td[2]/a').click()
    # xpath -> syntax to describe parts of xml documents
    with open("stars.csv" , "w" )as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planet_data)
scrape()

