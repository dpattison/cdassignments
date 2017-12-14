from django.shortcuts import render, redirect
from django.http import HttpResponse


def index(request):
    response = "placeholder to later display all the list of users"
    return HttpResponse(response)

def register(request):
    response = "placeholder for users to create a new user record"
    return HttpResponse(response)

def login(request):
    response = "placeholder for users to login"
    return HttpResponse(response)