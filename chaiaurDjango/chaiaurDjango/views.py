from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("hello, world. You are at chai aur Django Home Page")
    return render(request, "website/index.html" )

def about(request):
    return render(request,"website/about.html")

def contact(request):
    return HttpResponse("Hello world. ypu are at chai django contact page")