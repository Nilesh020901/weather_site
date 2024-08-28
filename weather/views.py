from django.shortcuts import render
# import json to load json data to python dictionary 
import json
# urllib.request to make a request to api 
import urllib.request

# Create your views here.

def index(request):
    if request.method=="POST":
        city=request.POST['city']
        # source contain JSON data from API 
        source=urllib.request.urlopen