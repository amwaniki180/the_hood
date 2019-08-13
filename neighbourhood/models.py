from __future__ import unicode_literals
from django.db import models
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

   def save_project(self):
       """
       This is the function that we will use to save the instance of this class
       """
       self.save()

   def delete_project(self):
       """
       This is the function that we will use to delete the instance of this class
       """
       self.delete()
    
   def get_absolute_url(self): 
        return reverse('home') 


   def __str__(self):
        return self.name
class Profile(models.Model):
    profile_image = models.ImageField(blank=True,upload_to='profiles/')
    bio = models.TextField(blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    neighbour_hood = models.ForeignKey(Project,on_delete = models.CASCADE,null=True)

    def save_profile(self):
        self.save()

    @classmethod
    def get_by_id(cls, id):
        profile = Profile.objects.get(user = id)
        return profile

    def filter_by_id(cls, id):
        profile = Profile.objects.filter(user = id).first()
        return profile

    def get_absolute_url(self): 
        return reverse('user_profile')
    
    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

class Business(models.Model):
    about = models.TextField(max_length=100)
    name = models.TextField(max_length=15)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='business')
    neighbourhood = models.ForeignKey(Project,on_delete = models.CASCADE)

    def save_business(self):
        self.save()

      
    @classmethod
    def get_by_id(cls, id):
        business = Business.objects.get(id = id)
        return profile

    
    def get_absolute_url(self): 
        return reverse('business')

    def __str__(self):
        return self.name

    @classmethod
    def get_business(cls, id):
        business = Business.objects.filter(neighbourhood__pk =id)
        return business

    @classmethod
    def search_business(cls,name):
        business = Business.objects.filter(name__icontains = name)
        return business
    def delete_business(self):
       Business.objects.get(id = self.id).delete()

class Post(models.Model):
    body = models.TextField()
    title = models.TextField(max_length=15)
    poster= models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')
    post_neighbourhood = models.ForeignKey(Project,on_delete = models.CASCADE)
    date = models.DateTimeField(auto_now_add = True,null = True)
    
    def save_post(self):
        self.save()

      
    @classmethod
    def get_by_id(cls, id):
        post = Post.objects.get(id = id)
        return post

    def delete_post(self):

        self.delete()
    
    def __str__(self):
        return self.title 
    
    @classmethod
    def get_post(cls, id):
        posts = Post.objects.filter(post_neighbourhood__pk =id)
        return posts