from django.urls import path

from . import views

app_name = 'ninjagold'

urlpatterns = [
    path('', views.index, name='index'),
    path('processmoney/', views.processmoney, name='processmoney'),
    path('reset/', views.reset, name='reset')
    ]