from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home_view(request):
    return HttpResponse("<h1> Home page </h1>")

def about_view(request):
    return HttpResponse("<h1> about page </h1>")

def contact_view(request):
    return HttpResponse("<h1> contact page </h1>")
