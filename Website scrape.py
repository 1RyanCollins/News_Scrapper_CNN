#website scraping

import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import docx

#Request webpage 
from requests import get
url = "https://www.cnn.com/2020/05/31/sport/michael-jordan-george-floyd-statement-trnd/index.html"




response = get(url)

print(response.text[:500])

soup = BeautifulSoup(response.text, 'html.parser')


result = soup.find_all(class_="zn-body__paragraph")



#Create a variable for word 
mydoc = docx.Document()

#write text onto a word doc
for tag in result:
    mydoc.add_paragraph(tag.text.strip())

#Export word doc

mydoc.save('C:/Users/rc124/Desktop/CNN.doc")
