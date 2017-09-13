from django.shortcuts import render
from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponse, HttpResponseNotFound
from instructors.models import Instructor

# Create your views here.


def hello(request):
    return render(request, "index.html")

def instructors_list(request):
    instructors = Instructor.objects.all()
    return render(request, "instructors.html", {"instructors_list" : instructors})

def http(request):
    print(dir(request))
    print(request.path)
    print(request.method)
    print(request.GET)
    print(request.POST)
    #print(request.META)
    return render(request, "http.html")     
    
def hello_python(request):
    return render(request, "python.html")

def sum_two(request, a, b):
    s = int(a) + int(b)
    return HttpResponse(s)