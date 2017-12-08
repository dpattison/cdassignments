from django.shortcuts import render, redirect
from django.http import HttpResponse


def index(request):
    return render(request, 'session_words/index.html')

def process(request):
    request.session['word'] = request.POST['word']
    request.session['color'] = request.POST['color']
    request.session['big'] = request.POST['big']
    return redirect('session_words:index')

def clear(request):
    request.session['words'] = []
    return redirect('session_words:index')