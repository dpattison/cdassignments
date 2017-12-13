from django.shortcuts import render, redirect
from django.http import HttpResponse
from time import strftime, localtime


def index(request):
    return render(request, 'session_words/index.html')

def process(request):
    words = request.session.get('words', [])
    newword = {
        'word': request.POST['word'],
        'color': request.POST['color'],
        'size': request.POST['size'],
        'time': strftime("%I:%M %p, %b %d %Y", localtime())
    }
    words.append(newword)
    request.session['words'] = words
    return redirect('session_words:index')

def clear(request):
    request.session.flush()
    return redirect('session_words:index')
