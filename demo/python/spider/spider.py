from urllib.request import urlopen
from bs4 import BeautifulSoup as bf
from urllib.request import urlretrieve

html = urlopen("https://store.steampowered.com/vr/")
# html_text = bytes.decode(html.read())
html_bf = bf(html.read(), 'html.parser')
html_title = html_bf.head.title

print(html_title)
game_pic = html_bf.find_all('img', class_="tab_item_cap_img")
count = 0

for i in game_pic:
    print(i['src'])
    count += 1;
    urlretrieve(i['src'], './tmp/'+str(count)+'.jpg')