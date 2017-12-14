from django.shortcuts import render, redirect
from django.http import HttpResponse


def index(request):
    response = "placeholder to display all the surveys created"
    return HttpResponse(response)

def new(request):
    response = "placeholder for users to add a new survey"
    return HttpResponse(response)


def process(request):
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']

    counter = request.session.get('count', 0)
    counter += 1
    request.session['count'] = counter
    return redirect('surveys:result')

def result(request):
    return render(request, 'surveys/result.html')