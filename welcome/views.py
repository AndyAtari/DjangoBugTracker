import re
from django.utils.timezone import datetime
from django.shortcuts import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, "welcome/home.html")

def welcome_there(request, name):
    return render(
        request,
        'welcome/welcome_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )

def about(request):
    return render(request, "welcome/about.html")

def tracker(request):
    return render(request, "welcome/tracker.html")