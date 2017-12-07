from django.urls import include, path
from . import views

app_name = 'blogs_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new),
    path('create/', views.create),
    path('<int:blog_id>/', views.show),
    path('<int:blog_id>/edit/', views.edit),
    path('<int:blog_id>/delete/', views.destroy)
]