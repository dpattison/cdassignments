from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string


# Create your views here.
def index(request):
    context = {
        "random": get_random_string(length=14)
        }
    return render(request,'random_word/index.html', context)
def reset(request):
    context = {
        "date": "reset time",
        "time": strftime("%I:%M %p", localtime())
        }
    return render(request,'random_word/index.html', context)