from django.shortcuts import render
from django.http import HttpResponse

def create(request):
    return HttpResponse("create")

def all_objects(request):
    return HttpResponse("all objects")