import requests
from bs4 import BeautifulSoup as BSoup
import pdb 
import json
from django.shortcuts import render , redirect , reverse
import urllib.request
from .models import App
from google_play_scraper import app , Sort , reviews







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
			print("error in requesting data")
	soup = BSoup(all_data , "html.parser")
	
	tags = soup.find_all('div' , {'class':"b8cIId ReQCgd Q9MA7b"})
	tags = set(tags)
	
	
	for tag in tags :
		try :
			#pdb.set_trace()
		
			db_app = App()
			main = tag.find_all('a')[0]
			link = main['href']
			google_play_id = link.split("=")
			google_id = google_play_id[1]
			#print(google_id)
			app_details = app(google_id)
			
			db_app.title = app_details["title"]
			db_app.google_play_id = app_details["appId"]
			check_if_present = duplicate_check(app_details["title"])
			if check_if_present :
				print("duplicate found")
				continue
			db_app.url = app_details["url"]
			db_app.ratings = app_details["score"]
			db_app.description = app_details["description"]
			db_app.size = app_details["size"]
			db_app.developer_name = app_details["developer"]
			db_app.image = app_details["icon"]
			db_app.androidVersion = app_details["androidVersion"]
			db_app.release_date = app_details["released"]
			db_app.genere = app_details["genre"]
			screenshot_list = []
			review_list = []
			screenshot_count = 0
			review_count = 0
			try :
				for screenshot in app_details["screenshots"] :
					screenshot_count +=1
					if screenshot_count <= 3 :
						screenshot_list.append(screenshot) 
				db_app.screenshot_link_1 = screenshot_list[0]
				db_app.screenshot_link_2 = screenshot_list[1]	
				db_app.screenshot_link_3 = screenshot_list[2]
			except :
				pass
			#pdb.set_trace()	
			try :
				
				result_review ,continuation_token= reviews(google_id,count=3)
				#pdb.set_trace()
				for one in result_review :
					review_list.append(one['content'])
				db_app.review_1 = review_list[0]
				db_app.review_2 = review_list[1]
				db_app.review_3 = review_list[2]	
					
				#for one_review in result_review :
					#print (one_review["content"])
			except :
			
				pass		
			db_app.save()		
		except :
			pass				
			
		
			
	return redirect("../") 






	
def duplicate_check(title):

	duplicate_slugs = App.objects.filter(title= str(title))
	
	try :
		if str(duplicate_slugs[0]) == str(links) :
			
			return True
		else :
			return False	
	except :
		pass		






def details_view(request,object_id):
	
	app_specific = App.objects.get(id = object_id)
	return redirect(reverse('details_redirect') + '?app=%s' %(app_specific.google_play_id))




def details_redirect(request ):
	print("Inside the details_redirect request")
	
	url_parameter = request.GET.get("app")
	app_specific = App.objects.get(google_play_id = url_parameter)
	context = {'item':app_specific}
	return render(request , "details_view.html" ,context =context) 
