import re
from django.utils.timezone import datetime
from django.shortcuts import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("Welcome, Trooper!")

def welcome_there(request, name):
    return render(
        request,
        'welcome/welcome_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )