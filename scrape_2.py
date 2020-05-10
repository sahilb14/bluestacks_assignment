import requests
from bs4 import BeautifulSoup as BSoup
import pdb 
import json
import urllib.request
from selenium import webdriver
from requests_html import HTMLSession
from google_play_scraper import app


PARAMS = ""
try :

	url = "https://play.google.com/store/apps/collection/topselling_free"
	r = requests.get(url) 
	all_data = r.content
except :
	print("URL ERROR")



soup = BSoup(all_data , "html.parser")
#print(soup.prettify())
#pdb.set_trace()
tags = soup.find_all('div' , {'class':"b8cIId ReQCgd Q9MA7b"})

tags = set(tags)

#pdb.set_trace()
for tag in tags :
	#pdb.set_trace()
	main = tag.find_all('a')[0]
	title = tag.find_all('div' , {'class' :"WsMG1c nnK0zc"})[0]
	title = title['title']
	link = main['href']
	google_play_id = link.split("=")[1]
	print (google_play_id)
	result = app(google_play_id)
	print(result["title"])
	