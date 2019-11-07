from django.db import models

class Friend(models.Model):
	image = models.ImageField(upload_to='image/')
	character = models.CharField(max_length=300)