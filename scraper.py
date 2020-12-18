import requests
from bs4 import BeautifulSoup
import json

file = open("out.txt", "w")
URL = 'https://www.lovefoodhatewaste.com/article/food-storage-a-z'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
items = []
for each_div in soup.findAll('div',{'class':'card-body'}):
    itemname = "none"
    itemstorage = "none"
    itemmorestorageinfo = "none"
    itemfreeze = "none"
    freezemoreinfo = "none"
    fresherforlonger = "none"
    itemname = each_div.find('h2', {'class':'card-title'}).text
    cardadvice = each_div.findAll('span',{'class':'card-advice'})
    itemstorage = cardadvice[0].text
    itemmorestorageinfo = cardadvice[1].text
    itemfreeze = cardadvice[2].text
    if(len(cardadvice) > 4):
        freezemoreinfo = cardadvice[3].text
        fresherforlonger = cardadvice[4].text
    items.append({
        "name" : itemname,
        "storage" : itemstorage,
        "itemmorestorageinfo" : itemmorestorageinfo,
        "freeze" : itemfreeze,
        "freezemoreinfo" : freezemoreinfo,
        "fresherforlongerinfo" : fresherforlonger
    })
file.write(json.dumps(items, indent=4))