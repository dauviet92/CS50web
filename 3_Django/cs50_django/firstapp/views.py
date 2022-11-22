from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "hello/index.html")

def index1(request):
    return HttpResponse("<h1 style=\"color:blue\">Hello, world!</h1>")

def viet(request):
    return HttpResponse("Hello, Viet!")

def truc(request):
    return HttpResponse("Hello, Truc!")

def greet(request, name):
    return render(request, "hello/greet.html",{
        "name": name.capitalize()
    })

def greet1(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")