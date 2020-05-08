import requests
from bs4 import BeautifulSoup as BSoup
import pdb 
import json
from django.shortcuts import render , redirect
import urllib.request
from .models import App







def render_landing_page(request):
	#all_apps = App.objects.all().delete()
	all_apps = App.objects.all()[::-1]
	context = {
	'object_list' : all_apps,
	}
	return render(request , "landing_page/home.html" , context)


def scrape(request):
	PARAMS = ""
	
	count = 0
	try :

		url = "https://play.google.com/store/apps/collection/topselling_free"
		r = requests.get(url) 
		all_data = r.content
	except :
			pass
	soup = BSoup(all_data , "html.parser")
	
	tags = soup.find_all('div' , {'class':"b8cIId ReQCgd Q9MA7b"})
	
	
	for tag in tags :
		
		app = App()
		main = tag.find_all('a')[0]
		title = tag.find_all('div' , {'class' :"WsMG1c nnK0zc"})[0]
		app.title = title['title']

		link = main['href']
		google_play_id = link.split("=")
		google_id = google_play_id[1]
		app.google_play_id = google_id
		url_2 = "https://play.google.com" + link	
	
		app.slug = url_2
		
		check_if_present = duplicate_check(url_2)
		if check_if_present:
			continue

		r_2 = requests.get(url_2)
		app_data = r_2.content
		soup_2 = BSoup(app_data , "html.parser")

		image_tag = soup_2.find_all('img' , {'class':"T75of sHb2Xb"})[0]
		image_icon_link = image_tag['src']
		app.image = image_icon_link
		screenshot_links_tag = soup_2.find_all('img', {'class' : "T75of DYfLw"})
		count = 0
		screenshot_link_list = []
	
		for screenshot in screenshot_links_tag :
		
			
			count = count+1
			try :
				if screenshot['src'] :
					screenshot_link_list.append(screenshot['src'])
			except :
				screenshot_link_list.append(screenshot['data-src'])	
			if count >=3 :
				break
		app.screenshot_link_1 = screenshot_link_list[0]
		app.screenshot_link_2 = screenshot_link_list[1]
		app.screenshot_link_3 = screenshot_link_list[2]
			

		description_tag = soup_2.find_all('meta',{'itemprop':"description"})[0]
		app.description = description_tag["content"]
		app.save()
		
			
	return redirect("../") 






	
def duplicate_check(links):

	duplicate_slugs = App.objects.filter(slug= str(links))
	
	try :
		if str(duplicate_slugs[0]) == str(links) :
			
			return True
		else :
			return False	
	except :
		pass		






def details_view(request , object_id):
	
	app_specific = App.objects.get(id = object_id)
	print(app_specific.title , app_specific.image , app_specific.slug ,app_specific.screenshot_link_1
		,app_specific.screenshot_link_2,app_specific.screenshot_link_3)
	context = {'item' : app_specific}
	return render(request , "details_view.html", context = context)