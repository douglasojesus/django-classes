from django.urls import path, include
from .views import *

urlpatterns = [
    path('all/', exibe_todos_profs),
    path('all/<int:ra>', exibe_prof_especifico)
]
