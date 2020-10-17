from django.db import models

# Create your models here.

class Blog(models.Model):
	title=models.CharField(max_length=50)
	pub_date=models.DateField(auto_now_add=True)
	body=models.CharField(max_length=500)

	def __str__(self):
		return self.title

	def summary(self):
		return self.body[:100]
