from django.db import models
from __future__ import unicode_literals
from django.contrib.auth.models import User
import datetime as dt
from tinymce.models import HTMLField
from django.dispatch import receiver
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.conf import settings
from django.db.models.signals import post_save


# Create your models here.
class Project(models.Model):
   """
   This is the class we will use to create images
   """
   image_url = models.ImageField(upload_to = "images/")
   name = models.CharField(max_length = 30)
   description = models.TextField(max_length=100)
   admin = models.ForeignKey(User,related_name='images',on_delete=models.CASCADE)
   date = models.DateTimeField(auto_now_add = True,null = True)
   location = models.CharField(max_length = 30)
   occupants = models.IntegerField(default = 0)