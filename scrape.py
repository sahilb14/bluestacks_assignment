import requests
from bs4 import BeautifulSoup as BSoup
import pdb 
import json
import urllib.request
from selenium import webdriver
from requests_html import HTMLSession


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
	google_play_id = link.split("=")
	url_2 = "https://play.google.com" + link
	pdb.set_trace()
	



	


	

	r_2 = requests.get(url_2)
	app_data = r_2.content
	
	soup_2 = BSoup(app_data, "html.parser")

	count_reviews = 0
	reviews = soup_2.find_all('div',{'class':"UD7Dzf"})
	for review in reviews :
		count_reviews +=1
		if count_reviews <=2 :
			print(review)
		else :
			break		





	image_tag = soup_2.find_all('img' , {'class':"T75of sHb2Xb"})[0]
	image_icon_link = image_tag['src']
	screenshot_links_tag = soup_2.find_all('img', {'class' : "T75of DYfLw"})
	count = 0
	screenshot_link_list = []
	try :
		for screenshot in screenshot_links_tag :
			count +=1 		
			
			screenshot_link_list.append(screenshot['src'])
			if count >= 3 :
				break
	#app.screenshot_link_1 = screenshot_link_list[0]
	#app.screenshot_link_2 = screenshot_link_list[1]
	#app.screenshot_link_3 = screenshot_link_list[2]
					
		for screenshot in screenshot_links_tag :
			screenshot_link = screenshot["src"]
	except :
		pass		
	description_tag = soup_2.find_all('meta',{'itemprop':"description"})[0]
	description = description_tag["content"]
	
	developer_name = soup_2.find_all('a' , {'class':"hrTbp euBY6b"})[0]
	developer_name = developer_name["href"].split(":")
	developer_name = developer_name[1]
	
	ratings = soup_2.find_all('div' , {'class':"BHMmbe"})[0]
	ratings = ratings["aria-label"]
	
	pdb.set_trace()
	count_reviews = 0
	reviews = soup_2.find_all('div',{'class':"UD7Dzf"})
	for review in reviews :
		count_reviews +=1
		if count_reviews <=2 :
			print(review)
		else :
			break		


def dynamic_scraping_js(url):
	pdb.set_trace()
	browser = webdriver.Chrome()
	browser.get(url)
	html = browser.page_source

	print(html)	



#apps = soup.find_all('div', {"class":"curation-module__item"})
#print (apps)
 
#News = soup.find_all('div', {"class":"curation-module__item"})