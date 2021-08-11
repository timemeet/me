# from urllib.request import urlopen
#from urllib import request
import urllib.request
import urllib.parse
import http.cookiejar
import os, time
from bs4 import BeautifulSoup as bf
from urllib.request import Request, urlretrieve
# selenium related
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


vr_url = 'https://store.steampowered.com/search/?sort_by=Released_DESC&tags=-1&vrsupport=402'
page_scroll_n = 3
game_ret_box = 'a'
game_ret_class = 'search_result_row'
game_ret_name_box = 'span'
game_ret_name_class = 'title'

# game info
game_info = {}
game_all = []

# start chrome
browser = webdriver.Chrome()
browser.get(vr_url)

while page_scroll_n > 0:
    time.sleep(1)
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(1)
    page_scroll_n = page_scroll_n - 1

# resp = urllib.request.urlopen(req)
html = browser.page_source
html_bf = bf(html, 'html.parser')
html_title = html_bf.head.title

# print dialog
print(html_title)
count = 0
game_box = html_bf.find_all(game_ret_box, class_=game_ret_class)
for i in game_box:
    print(i['href'])
    count += 1;
    game_info['href'] = i['href']
    game_info['data-ds-itemkey'] = i['data-ds-itemkey']
    game_all.append(game_info)

# make diretory
time_str = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
path_dir = './tmp/' + time_str + '/'
os.mkdir(path_dir)
# download feature pics
game_pic = html_bf.find_all('img', class_="tab_item_cap_img")
count = 0
for i in game_pic:
    print(i['src'])
    count += 1;
    urlretrieve(i['src'], path_dir+str(count)+'.jpg')
print(str(count)+' pics'+ ' stored into' + path_dir)

# close browser
browser.close()

