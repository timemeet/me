# from urllib.request import urlopen
#from urllib import request
import urllib.request
import urllib.parse
import http.cookiejar
import os, time
from bs4 import BeautifulSoup as bf
from urllib.request import Request, urlretrieve
from selenium import webdriver

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

# start chrome
browser = webdriver.Chrome()