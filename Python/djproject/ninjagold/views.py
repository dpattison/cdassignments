from django.shortcuts import render, redirect
from django.http import HttpResponse
from time import strftime, localtime
from random import randint


def index(request):
    total_gold = request.session.get('total_gold', 0)
    request.session['total_gold'] = total_gold
    return render(request, 'ninjagold/index.html', )


def processmoney(request):
    total_gold = request.session['total_gold']
    messages = request.session.get('messages', [])
    location = (request.POST['location'])
    if location == "farm":
        gold = randint(10, 20)
    elif location == "cave":
        gold = randint(5, 10)
    elif location == "house":
        gold = randint(2, 5)
    elif location == "casino":
        gold = randint(-50, 50)
    total_gold += gold
    request.session['total_gold'] = total_gold
    time = strftime("%I:%M %p %b %d, %Y", localtime())
    if gold > 0:
        messages.insert(0,"Earned " + str(gold) + " gold from the " + location + "! (" + time + ")")
    else:
        messages.insert(0,"Entered a casino and lost " + str(abs(gold)) + " gold.. Ouch! (" + time + ")")
    request.session['messages'] = messages
    return redirect('ninjagold:index')


def reset(request):
    request.session.flush()
    return redirect('ninjagold:index')
