from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string


# Create your views here.
def index(request):
    context = {
        "random": get_random_string(length=14)
        }
    counter = request.session.get('count', 0)
    counter += 1
    request.session['count'] = counter
    return render(request,'random_word/index.html', context)
def reset(request):
    request.session['count'] = 0
    return redirect('random_word:index')