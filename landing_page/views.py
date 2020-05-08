import requests
from bs4 import BeautifulSoup as BSoup
import pdb 
import json
from django.shortcuts import render


import urllib.request
from .models import App



#pdb.set_trace()
#session = requests.Session()



def render_landing_page(request):
	#scrape_data = scrape(request)
	#all_apps = App.objects.all().delete()
	all_apps = App.objects.all()[::-1]
	context = {
	'object_list' : all_apps,
	}
	return render(request , "landing_page/home.html" , context)


def scrape(request):
	PARAMS = ""
	current_page = 1
	total_count = 50 
	while current_page <= total_count /50 :
		try :

			url = "https://play.google.com/store/apps/collection/topselling_free"
			r = requests.get(url) 
			all_data = r.content
		except :
			print("URL ERROR")
		soup = BSoup(all_data , "html.parser")
	
		tags = soup.find_all('div' , {'class':"b8cIId ReQCgd Q9MA7b"})

		for tag in tags :
			app = App()
	
			main = tag.find_all('a')[0]
			title = tag.find_all('div' , {'class' :"WsMG1c nnK0zc"})[0]
			app.title = title['title']
		
			link = main['href']
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
			#screenshot_links_tag = soup_2.find_all('img', {'class' : "T75of DYfLw"})
			#print(screenshot_links_tag)
			#count = 0
			#screenshot_link_list = []
			#while (count <= 3):
				#for screenshot in screenshot_links_tag :
					#print(screenshot['src'])
					#count = count+1
					#screenshot_link_list.append(screenshot['src'])
			#app.screenshot_link_1 = screenshot_link_list[0]
			#app.screenshot_link_2 = screenshot_link_list[1]
			#app.screenshot_link_3 = screenshot_link_list[2]
					

			description_tag = soup_2.find_all('meta',{'itemprop':"description"})[0]
			app.description = description_tag["content"]
			app.save()
	return redirect("../") 	



	
def duplicate_check(links):

	duplicate_slugs = App.objects.filter(slug = links)
	print(duplicate_slugs)
	try :
		if str(duplicate_slugs[0]) == str(links) :
			return True
	except :
		pass		






