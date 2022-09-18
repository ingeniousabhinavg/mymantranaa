from contextlib import nullcontext
from distutils.text_file import TextFile
from django.db import models

# Create your models here.

class Services(models.Model):
    service = models.CharField(max_length=50, null=False)
    banner = models.ImageField(upload_to ='services', null=False)
    about = models.TextField()
    created_on = models.DateField(auto_now=False, auto_now_add=False, null=False)

    def __str__(self) -> str:
        return self.service

class Counsellors(models.Model):
    name = models.CharField(max_length=50, null=False)
    profile_pic = models.ImageField(upload_to='counsellors', max_length=50, null=False)
    joined_on = models.DateField(auto_now=False, auto_now_add=False, null=False)
    experties = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
