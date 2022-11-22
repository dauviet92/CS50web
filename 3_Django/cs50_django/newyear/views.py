import datetime as dt 

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    now = dt.datetime.now()
    return render(request, "newyear/index.html", {
        "newyear": now.month==1 and now.day==1
    })

    