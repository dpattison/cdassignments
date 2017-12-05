from django.shortcuts import render, HttpResponse, redirect
from time import strftime, localtime
from django.utils import timezone


# Create your views here.
def index(request):
    context = {
        "date": strftime("%b %d, %Y", localtime()),
        "time": strftime("%I:%M %p", localtime())
        }
    return render(request,'time_display/index.html', context)