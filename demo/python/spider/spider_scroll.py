# from urllib.request import urlopen
#from urllib import request
import urllib.request
import urllib.parse
import http.cookiejar
import os, time
import re
from bs4 import BeautifulSoup as bf
from urllib.request import Request, urlretrieve
# selenium related
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# set env
#cur_path = os.environ['PATH']
#os.environ['PATH'] = cur_path + ';' +  

# func
def getValByClass(pattern, source, *result):
    result = source.find_all(class_=re.compile(pattern))
    if len(result) == 0:
        print("error: ",__file__,sys._getframe().f_lineno)
    return len(result)

vr_url = 'https://store.steampowered.com/search/?sort_by=Released_DESC&tags=-1&vrsupport=402'
page_scroll_n = 3
game_ret_box = 'a'
game_ret_class = 'search_result_row'
game_ret_name_box = 'span'
game_ret_name_class = 'title'

# game info
game_info = {}
game_all = []



# start browser
driver_url = './env/msedgedriver.exe'
os.environ["webdriver.Edge.driver"] = driver_url
browser = webdriver.Edge(executable_path=driver_url)
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
game_basic = []
game_id = 0
game_box = html_bf.find_all(game_ret_box, class_=game_ret_class)
game_de_sr = []
print('total game: ' + str(len(game_box)))
for i in game_box:
    count += 1;
    # find info from href 
    game_basic = re.findall(r'/app/(\d+)/(.+?)/', str(i['href']))
    print('No.' + str(count) + ': ')
    print('---- ' + i['href'])
    print('len: ' + str(len(game_basic)))
    # href not match, break
    if len(game_basic) == 0:
        break
    
    # get basic info from href
    game_info['id'] = game_basic[0][0]
    game_info['name_abbr'] = game_basic[0][1]
    game_info['href'] = i['href']
    # get more info from children
    # get name
    game_de_sr = i.find_all(class_=re.compile("title"))
    if len(game_de_sr) == 0:
        print("error: ",__file__,sys._getframe().f_lineno)
        break
    game_info['name'] = str(game_de_sr[0].text)

    # log
    print('id: ' + game_info['id'])
    print('name_abbr: ' + game_info['name_abbr'])
    print('name: ' + game_info['name'])
    




    # append info node to list
    game_all.append(game_info)
 
'''
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
'''

# close browser
browser.close()

