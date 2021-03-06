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

# construct request
url = 'https://store.steampowered.com/vr/'
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Host': 'store.steampowered.com'
}
req = Request(url=url, headers=headers, method='GET')

# send request
# resp = urllib.request.urlopen(req)
cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
html_opener = urllib.request.build_opener(handler)
resp = html_opener.open(req)
html = resp.read()
html_bf = bf(html, 'html.parser')
html_title = html_bf.head.title

# print dialog
print(resp.getheaders())
print(html_title)

# save cookie
html_cookie = {}
for i in cookie:
    html_cookie[i.name] = i.value
    print(i.name, i.value)

# start chrome
browser = webdriver.Chrome()
vr_url = 'https://store.steampowered.com/search/?sort_by=Released_DESC&tags=-1&vrsupport=402'
browser.get(vr_url)
page_scroll_n = 10
while page_scroll_n > 0:
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(1)
    page_scroll_n = page_scroll_n - 1


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

