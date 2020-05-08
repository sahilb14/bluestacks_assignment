from django.db import models

# Create your models here.


class App(models.Model):
	title = models.CharField(max_length = 200)
	image = models.URLField(null = True , blank = True)
	slug = models.URLField(null = False , blank = False)
	description = models.TextField(null = False)
	screenshot_link_1 = models.URLField(null = True , blank = True)
	screenshot_link_2 = models.URLField(null = True , blank = True)
	screenshot_link_3 = models.URLField(null = True , blank = True)


	def __str__(self):
		return self.title


