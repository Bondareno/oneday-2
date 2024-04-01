import datetime

from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render

from .models import News


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def news(request):
    n = News.objects.all().order_by('created')
    text = ""
    
    for i in n:
        text += f"<li>{i.case.name}, {i.oldtext}, {i.newtext}, {i.created}</li>"
    
    html = f"<html><body>{text}</body></html>"
    return HttpResponse(html)

def news2(request):
    n = News.objects.all().order_by('created')
    return render(request, "news_c.html", {'news': n})


def newsjson(request):
    n = News.objects.all().order_by('created')
    d = [{'case': i.case.name, "old": i.oldtext, 
           "new": i.newtext, "created": i.created} for i in n]
    return JsonResponse(d, safe=False)
