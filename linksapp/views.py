from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import HttpResponse, redirect
from .models import *
from django.http import JsonResponse
from datetime import datetime, time, date
from django.utils import timezone
import os



# Create your views here.

def viewlink(request,pk,title):
    obj=Createlinks.objects.get(id=pk)
    return render(request,"redirectionpage.html",{"obj":obj})

def index(request):
    current_time = current_time = timezone.now() 
    showLinks=ShowLinks.objects.all()[0]
    data=Createlinks.objects.filter(pin=False).order_by('-created_at')[:showLinks.numbers_to_show]
    pined=Createlinks.objects.filter(pin=True).order_by('-pin_created_Date')[:showLinks.pinned_numbers]
    favicon = os.getenv("FAVICON")
    logo = os.getenv("LOGO")
    BackgroundImage = os.getenv("BACKGROUND_IMAGE")
    mailIid=os.getenv("MAILID")
    twitterid=os.getenv("TWITTER")
    instagramid=os.getenv("INSTAGRAM")
    phone=os.getenv("PHONE")
    return render(request,"index.html",{"data":data,"pined":pined,"favicon":favicon,"logo":logo,"BackgroundImage":BackgroundImage,"mailIid":mailIid,"twitterid":twitterid,"instagramid":instagramid,"phone":phone})

