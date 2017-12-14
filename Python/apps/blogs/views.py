from django.shortcuts import render, HttpResponse, redirect


# Create your views here.
def index(request):
    response = "placeholder to later display all the list of blogs"
    return HttpResponse(response)
def new(request):
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)
def create(request):
    return redirect('blogs:index')
def show(request, blog_id):
    return HttpResponse("placeholder to display blog %s" % blog_id)
def edit(request, blog_id):
    return HttpResponse("placeholder to edit blog %s" % blog_id)
def destroy(request, blog_id):
    return redirect('blogs:index')