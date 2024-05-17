from django.contrib import admin
from django.urls import path, include
from .views import create, all_objects
from django.http import HttpResponse

urlpatterns = [
    path('', lambda request:HttpResponse("eventos")),
    path('create/', create),
    path('all/', all_objects),
]
