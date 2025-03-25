# Ex02 Django ORM Web Application
# Date:20/03/2025
# AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## DESIGN STEPS
## STEP 1:
Clone the problem from GitHub

## STEP 2:
Create a new app in Django project

## STEP 3:
Enter the code for admin.py and models.py

## STEP 4:
Execute Django admin and create details for 10 books

# PROGRAM
models.py
```
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
```
admin.py
``` 
from Django.contrib import admin
from .models import Bankloan,BankloanAdmin
admin.site.register(Bankloan,BankloanAdmin)
```
# OUTPUT


# RESULT
Thus the program for creating a database using ORM hass been executed successfully
