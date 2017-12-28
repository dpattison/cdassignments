from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    return render(request, 'login/index.html')

def register(request):
    new_user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=request.POST['password'])
    return redirect('success')

def login(request):
    response = "login"
    return HttpResponse(response)

def success(request):
    return render(request, 'login/success.html')