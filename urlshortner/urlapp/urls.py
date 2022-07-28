from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('create', views.add, name = 'create'),
    path('links', views.get_all, name = 'get_all'),
    path('<str:pk>', views.shorten, name = 'shorten'),

]