import re
from django.utils.timezone import datetime
from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from welcome.forms import LogMessageForm
from welcome.models import LogMessage

def home(request):
    return render(
        request, 
        "welcome/home.html",
        {
            'date': datetime.now()
        })

def about(request):
    return render(request, "welcome/about.html")

def tracker(request):
    form = LogMessageForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
    else:
        return render(request, "welcome/log_message.html", {"form": form})