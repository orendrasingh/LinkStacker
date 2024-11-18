from django.db import models
from django.contrib.auth.models import User 
from django.utils.timezone import *
from django.utils import timezone
import string
# Create your models here..

class Createlinks(models.Model):
    name = models.CharField(max_length=500, blank=True, default="")
    link= models.URLField(max_length=800, blank=True, default="")
    created_at= models.DateTimeField(default=timezone.now)
    modified_at= models.DateTimeField(auto_now=True)
    pin = models.BooleanField(default=False)
    pin_created_Date= models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name

class ShowLinks(models.Model):
    numbers_to_show = models.IntegerField(default=10)
    def __str__(self):
        return str(self.numbers_to_show)


