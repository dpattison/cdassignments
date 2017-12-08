from django.urls import path

from . import views

app_name = 'session_words'

urlpatterns = [
    path('', views.index, name='index'),
    path('process/', views.process, name='process'),
    path('clear/', views.clear, name='clear')
    ]