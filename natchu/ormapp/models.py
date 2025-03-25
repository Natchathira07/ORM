from django.db import models
from django.contrib import admin
class Bankloan(models.Model):
	accountnum=models.CharField(max_length=16,primary_key=True)
	name=models.CharField(max_length=100)
	principle=models.IntegerField()
	rate=models.IntegerField()
	time=models.IntegerField()

class BankloanAdmin(admin.ModelAdmin):
	list_display=('accountnum','name','principle','rate','time')

