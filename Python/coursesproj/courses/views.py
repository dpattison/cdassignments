from django.shortcuts import render, redirect
from django.http import HttpResponse

from courses.models import *


def index(request):
    return render(request, 'courses/index.html', { "courses": Course.objects.all() })

def create(request):
    new_course = Course.objects.create(name=request.POST['name'], description=request.POST['description'])
    id = new_course.id
    return redirect('index')

def destroy(request, id):
    return render(request, 'courses/remove.html', { "course": Course.objects.get(id = id)})


def delete(request, id):
    course = Course.objects.get(id = id)
    course.delete()
    return redirect('index')