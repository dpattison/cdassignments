from django.shortcuts import render, redirect
from django.http import HttpResponse
from time import strftime, localtime

items = [{"product_id": 1,"price": 19.99, "description":"Dojo Tshirt"}, {"product_id": 2,"price": 29.99, "description":"Dojo Sweater"},{"product_id": 3,"price": 4.99, "description":"Dojo Cup"},{"product_id": 4,"price": 49.99, "description":"Algorithm Book"}]


def index(request):
    return render(request, 'amadon/index.html', {'items': items})

def buy(request):
    items_ordered = request.session.get('items_ordered', 0)
    total_ordered = request.session.get('total_ordered', 0)
    pid = (request.POST['product_id'])
    quantity = int(request.POST['quantity'])
    for item in items:
        if item["product_id"] == int(pid):
            total = float(item["price"]) * quantity
    items_ordered += quantity
    total_ordered += total
    request.session['total'] = total
    request.session['items_ordered'] = items_ordered
    request.session['total_ordered'] = total_ordered
    return redirect('amadon:checkout')


def checkout(request):
    return render(request, 'amadon/checkout.html')

def reset(request):
    request.session.flush()
    return redirect('amadon:index')
