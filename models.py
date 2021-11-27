from django.db import models

# Create your models here.

class member(models.Model):
	Name=models.CharField(max_length=250)
	Age=models.IntegerField()
	Class=models.IntegerField()
