from django.db import models

# Create your models here.


class App(models.Model):
	title = models.CharField(max_length = 200)
	image = models.URLField(null = True , blank = True)
	url = models.URLField(null = False , blank = False)
	description = models.TextField(null = False)
	developer_name = models.CharField(null=True , max_length =200)
	ratings = models.CharField(null=True , max_length=200)
	google_play_id = models.CharField(max_length = 200  , null = True)
	screenshot_link_1 = models.URLField(null = True , blank = True)
	screenshot_link_2 = models.URLField(null = True , blank = True)
	screenshot_link_3 = models.URLField(null = True , blank = True)
	size = models.CharField(null= True , max_length=50)
	androidVersion = models.CharField(null = True , max_length= 50)
	genre = models.CharField(null=True , max_length=100)
	release_date = models.CharField(null =True , max_length=200)
	review_1 = models.CharField(null = True , max_length = 500)
	review_2 = models.CharField(null= True , max_length = 500)
	review_3 = models.CharField(null=True , max_length =500)






	def __str__(self):
		return self.slug


