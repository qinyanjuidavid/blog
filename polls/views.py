from django.shortcuts import render
from django.http import HttpResponse

def info(request):
    return HttpResponse("Hello world,i am abegginer in django rest framework.")
    

# Create your views here.
