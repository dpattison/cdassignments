from django.urls import include, path
from . import views

app_name = 'users'
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('<int:id>/edit', views.edit, name='edit'),
    path('<int:id>', views.show, name='show'),
    path('create/', views.create, name='create'),
    path('<int:id>/destroy', views.destroy, name='destroy'),
    path('<int:id>/update/', views.update, name='update')
]