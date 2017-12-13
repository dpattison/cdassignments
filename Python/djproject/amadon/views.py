from django.shortcuts import render, redirect
from django.http import HttpResponse
from time import strftime, localtime

items = [{"prouct_id": 1,"price": 19.99, "description":"Dojo Tshirt"}, {"prouct_id": 2,"price": 29.99, "description":"Dojo Sweater"},{"prouct_id": 3,"price": 4.99, "description":"Dojo Cup"},{"prouct_id": 4,"price": 49.99, "description":"Algorithm Book"}]


def index(request):
    return render(request, 'amadon/index.html')

def buy(request):
    request.session['product_id'] = request.POST['product_id'],
    request.session['quantity'] = request.POST['quantity']
    return redirect('amadon:checkout')


def checkout(request):
    return render(request, 'amadon/checkout.html')
