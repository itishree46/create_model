from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.

def topicinsert(request):
    t=input('enter topic name:')
    T=Topic.objects.get_or_create(topic_name=t)[0]
    T.save()
    return HttpResponse('topic name inserted successfully.')

def webpageinsert(request):
    t=input('enter topic name:')
    Name=input('enter  name:')
    Url=input('enter url')
    T=Topic.objects.get_or_create(topic_name=t)[0]
    T.save()
    W=Webpage.objects.get_or_create(topic_name=T,name=Name,url=Url)[0]
    W.save()
    return HttpResponse('webpage inserted successfully.')
def ARinsert(request):
    t=input('enter topic name:')
    Name=input('enter  name:')
    Url=input('enter url:')
    T=Topic.objects.get_or_create(topic_name=t)[0]
    T.save()
    W=Webpage.objects.get_or_create(topic_name=T,name=Name,url=Url)[0]
    W.save()
    d=input('enter date:')
    A=Access_Records.objects.get_or_create(name=W,date=d)[0]
    A.save()
    return HttpResponse('Access_Records inserted successfully')