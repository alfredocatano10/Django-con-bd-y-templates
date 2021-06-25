from django.db import models

class post (models.Model):
	name = models.CharField(default = "",null=True,max_length = 60)
	desc = models.CharField(default = "",null=True,max_length = 100)
	date = models.CharField(default = "",null=True,max_length = 20)
	img = models.ImageField(upload_to = "imagen", null="True")

	def __str__ (self):
		return self.name

class post2 (models.Model):
	name = models.CharField(default = "",null=True,max_length = 60)
	desc = models.CharField(default = "",null=True,max_length = 100)
	date = models.CharField(default = "",null=True,max_length = 20)
	img = models.ImageField(upload_to = "imagen", null="True")

	def __str__ (self):
		return self.name