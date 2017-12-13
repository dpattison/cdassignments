from django.urls import path

from . import views

app_name = 'amadon'

urlpatterns = [
    path('', views.index, name='index'),
    path('buy/', views.buy, name='buy'),
    path('checkout/', views.checkout, name='checkout'),
    path('reset/', views.reset, name='reset')
    ]