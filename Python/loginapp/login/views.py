from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages
import bcrypt

# Create your views here.
def index(request):
    return render(request, 'login/index.html')

def users(request):
    return render(request, 'login/users.html', { "users": User.objects.all() })

def register(request):
    pw = request.POST['password']
    confirmpw = request.POST['confirm_password']
    email = request.POST['email']
    if (confirmpw != pw):
        messages.error(request, 'Passwords do not match')
        return redirect('index')
    else:
        try:
            user = User.objects.get(email=email)
            messages.error(request, user.email + ' already exists')
            return redirect('index')
        except:
            hashedpw = bcrypt.hashpw(pw.encode('UTF-8'), bcrypt.gensalt())
            User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=email, password=hashedpw)
            request.session['first_name'] = request.POST['first_name']
            messages.success(request, 'Sucessfully registered')
            return redirect('success')

def login(request):
    email = request.POST['email']
    try:
        user = User.objects.get(email=email)
    except:
        messages.error(request, email + ' is not registered')
        return redirect('index')   
    if bcrypt.checkpw(request.POST['password'].encode('UTF-8'), user.password):
        request.session['first_name'] = user.first_name
        messages.success(request, 'Sucessfully logged in')
        return redirect('success')
    else:
        messages.error(request, 'Password is not correct for ' + email)
        return redirect('index')

def success(request):
    return render(request, 'login/success.html')

def destroy(request, id):
    user = User.objects.get(id = id)
    user.delete()
    return redirect('users')

