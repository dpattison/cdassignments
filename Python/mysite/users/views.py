from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from users.models import *


def index(request):
    return render(request, 'users/index.html', { "users": User.objects.all() })

def new(request):
    return render(request, 'users/new.html')

def edit(request, id):
    return render(request, 'users/edit.html', {"user": User.objects.get(id = id)} )

def show(request, id):
    return render(request, 'users/show.html', {"user": User.objects.get(id = id)} )

def create(request):
    new_user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
    id = new_user.id
    return redirect('/users/'+str(id))

def destroy(request, id):
    user = User.objects.get(id = id)
    user.delete()
    return redirect('users:index')

def update(request, id):
    user = User.objects.get(id = id)
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.email = request.POST['email']
    user.save()
    return redirect('/users/'+str(id))