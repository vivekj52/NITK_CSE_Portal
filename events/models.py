from django.db import models

class Workshops(models.Model):
	event = models.CharField(max_length = 100)
	title = models.CharField(max_length = 500)
	status = models.CharField(max_length = 50)
	duration = models.CharField(max_length = 50)
	dates = models.CharField(max_length = 50)
	organizers = models.CharField(max_length = 100)
	place= models.CharField(max_length = 100)

	def __str__(self):
			return self.title


class Conferences(models.Model):
	event = models.CharField(max_length = 50)
	title = models.CharField(max_length = 500)
	status = models.CharField(max_length = 50)
	sponsored = models.CharField(max_length = 50)
	duration = models.CharField(max_length = 50)
	dates = models.CharField(max_length = 50)
	organizers = models.CharField(max_length = 100)
	place = models.CharField(max_length = 100)
	websitelink = models.CharField(max_length=100)
	cfp = models.CharField(max_length=50)
	paperdue = models.CharField(max_length=50)	

	def __str__(self):
			return self.title

class News(models.Model):
	title = models.CharField(max_length = 500)
	description = models.TextField(max_length = 500)

	def __str__(self):
			return self.title