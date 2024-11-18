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
    num=ShowLinks.objects.all()[0]
    data=Createlinks.objects.filter()[:num.numbers_to_show]
    pined=Createlinks.objects.filter(pin=True, pin_created_Date__lte=current_time).order_by('-pin_created_Date')[:5]
    Notpined=Createlinks.objects.filter(pin=False)
    favicon = os.getenv("FAVICON")
    logo = os.getenv("LOGO")
    BackgroundImage = os.getenv("BACKGROUND_IMAGE")
    mailIid=os.getenv("MAILID")
    twitterid=os.getenv("TWITTER")
    instagramid=os.getenv("INSTAGRAM")
    phone=os.getenv("PHONE")
    return render(request,"index.html",{"Data":data,"pined":pined,"Notpined":Notpined,"favicon":favicon,"logo":logo,"BackgroundImage":BackgroundImage,"mailIid":mailIid,"twitterid":twitterid,"instagramid":instagramid,"phone":phone})

