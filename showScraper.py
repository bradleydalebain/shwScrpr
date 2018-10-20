''' #!/home/Documents/python/scraper-master/scrape3/python3.6 '''

import youtube_dl
import requests
from bs4 import BeautifulSoup
from pprint import pprint
from selenium import webdriver
import selenium.webdriver.chrome.service as service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import subprocess
uname = ''
psswd = ''
URL = 'http://www.cc.com/episodes/scdnse/stand-up-specials-carlos-mencia--no-strings-attached-season-1-ep-101'
options = webdriver.ChromeOptions()
options.binary_location='/usr/bin/google-chrome'
# options.add_argument('headless')
# options.add_argument('--proxy-server=192.168.43.1:8000')
browser = webdriver.Chrome(chrome_options=options)
browser.get(URL)
urls = []


def login(browser):
    unamefield = browser.find_element_by_xpath('//*[@id="container"]/div/table/tbody/tr/td/table/tbody/tr[2]/td[2]/form/input[1]')
    passfield = browser.find_element_by_xpath('//*[@id="container"]/div/table/tbody/tr/td/table/tbody/tr[2]/td[2]/form/input[2]')
    sub = browser.find_element_by_xpath('//*[@id="container"]/div/table/tbody/tr/td/table/tbody/tr[2]/td[2]/form/input[7]')
    unamefield.send_keys(uname)
    passfield.send_keys(psswd)
    sub.click()
    browser.switch_to_window(browser.window_handles[0])
    page = browser.current_url
    GetContent(browser)

def getlogin(browser):

    coxpage = browser.find_element_by_xpath('//*[@id="primaryListWrapper"]/ul/li[4]/a')
    coxpage.click()
    browser.switch_to_window(browser.window_handles[1])
    wait = WebDriverWait(browser, 120)
    wait.until(EC.presence_of_element_located((By.ID, 'pf-search-input')))
    login(browser)


def GetContent(browser):
    urls = []
    ydl_opts = {'config-location' : '~/.config/youtube-dl/youtube-dl.conf' , 'outtmpl': '~/Videos/surv/%(title)s.%(ext)s', 'external_downloader' : 'axel', 'external_downloader_args' : '-n 5'}
    src = browser.find_element_by_name('original-source')
    srctext = src.get_attribute('content')
    urls.append(src)
    print(srctext)
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([srctext])


getlogin(browser)
"""
proxies = {
'http' : 'http://192.168.43.1:8000',
'https' : 'https://192.168.43.1:8000',
}
"""
