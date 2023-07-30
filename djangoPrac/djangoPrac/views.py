from django.http import HttpResponse
from django.shortcuts import render

def aboutUs(request):
    return HttpResponse ("manish")

def info(request):
    return HttpResponse ("dhamai")

def details(request,new):
    return HttpResponse (new)

def homePage(request):
    return render(request,"index.html")
