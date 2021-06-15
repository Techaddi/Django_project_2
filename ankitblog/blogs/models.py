from django.db import models
from django.db.models.fields import AutoField
import datetime

# Create your models here.


class Title(models.Model):
    headings = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)

class Blog(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)
    postedby= models.CharField(max_length=100)
    date= datetime.datetime.now()
    img= models.ImageField(upload_to='pics')
    explain= models.TextField(max_length=2000)

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(max_length=200)

class About(models.Model):
    head= models.CharField(max_length=100)
    about=models.TextField(max_length=1000)

class Welcome(models.Model):
    head= models.CharField(max_length=100)
    desc= models.TextField(max_length=500)
    



