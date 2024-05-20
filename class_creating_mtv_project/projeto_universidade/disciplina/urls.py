from django.urls import path, include
from .views import *

urlpatterns = [
    path('all/', exibe_todos_disc),
    path('all/<str:codigo>', exibe_disc_especifico)
]
