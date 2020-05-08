import requests
from bs4 import BeautifulSoup as BSoup
import pdb 
import json
import urllib.request

#pdb.set_trace()
#session = requests.Session()
PARAMS = ""
try :

	url = "https://play.google.com/store/apps/collection/topselling_free"
	r = requests.get(url) 
	all_data = r.content
except :
	print("URL ERROR")



soup = BSoup(all_data , "html.parser")
#print(soup.prettify())
pdb.set_trace()
tags = soup.find_all('div' , {'class':"b8cIId ReQCgd Q9MA7b"})
#pdb.set_trace()
for tag in tags :
	pdb.set_trace()
	main = tag.find_all('a')[0]
	title = tag.find_all('div' , {'class' :"WsMG1c nnK0zc"})[0]
	title = title['title']
	link = main['href']
	url_2 = "https://play.google.com" + link
	r_2 = requests.get(url_2)
	app_data = r_2.content
	soup_2 = BSoup(app_data , "html.parser")
	#pdb.set_trace()
	image_tag = soup_2.find_all('img' , {'class':"T75of sHb2Xb"})[0]
	image_icon_link = image_tag['src']
	screenshot_links_tag = soup_2.find_all('img', {'class' : "T75of DYfLw"})
	for screenshot in screenshot_links_tag :
		screenshot_link = screenshot["src"]
	description_tag = soup_2.find_all('meta',{'itemprop':"description"})[0]
	description = description_tag["content"]

	
	



#apps = soup.find_all('div', {"class":"curation-module__item"})
#print (apps)
 
#News = soup.find_all('div', {"class":"curation-module__item"})