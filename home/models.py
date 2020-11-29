from django.db import models
from django.utils import timezone



class Products(models.Model):
	img_name = models.CharField(max_length=20)
	img_file = models.ImageField(default="logo.jpg", upload_to='images/') 
	description = models.CharField(default="", max_length=500)


class Sample(models.Model):
	name = models.CharField(default="", max_length=500)
	description = models.CharField(max_length=100)
	address = models.CharField(default="", max_length=100)
	contact_no = models.CharField(default="", max_length=10)
	email = models.CharField(default="", max_length=20)

class Logo(models.Model):
	img_name = models.CharField(max_length=20)
	img_file = models.ImageField(default="logo.jpg", upload_to='images/') 
	description = models.CharField(default="", max_length=500)

	def __str__(self):
		return self.img_name