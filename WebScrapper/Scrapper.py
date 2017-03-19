import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui
import selenium.webdriver.support.expected_conditions as EC
import os
import time
from bs4 import BeautifulSoup
import urllib.request


class siteScrapper():
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        dir_path = os.path.dirname(os.path.realpath(__file__))
        chromedriver = dir_path +"/chromedriver"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver= webdriver.Chrome(chrome_options=options, executable_path=chromedriver)

    def timerControl(self):
        time.sleep(10)

    def gotoParentUrl(self): #selects US radio button- hardcoded
        self.driver.get("http://whed.net/search_by_region.php?region=North+America#")
        self.driver.find_element_by_css_selector("#contenu > form > div > div:nth-child(3) > ul > li:nth-child(1) > a").click()

    def expandSection(self):
        self.driver.find_element_by_xpath("//*[@id=\"results\"]/li[1]/div[2]/p[4]/a").click()
        wait = WebDriverWait(driver, 10)
       # element = wait.until(EC.element_to_be_clickable((By.ID, 'someid')))

    def gotoInstituteUrl(self, id):
        #self.driver.get("http://whed.net/detail_institution.php?id="+id)
        r = urllib.request.urlopen('http://whed.net/detail_institution.php?id='+id).read()
        soup = BeautifulSoup(r,"lxml")
        #print(soup.prettify())
        #print(r)
        keys = soup.find_all("div", class_="dt")
        print(keys[1])



    def teardown(self):
        self.driver.close()



if __name__ =="__main__":
    obj = siteScrapper()
    #obj.gotoParentUrl()
    #obj.expandSection()
    obj.gotoInstituteUrl(str(9))
    obj.timerControl()
    #obj.teardown()


#a = requests.get('http://whed.net/home.php')

#print(a.text)
#driver = webdriver.Firefox()