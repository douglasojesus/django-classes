from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def meu_app_view2(request):
    return HttpResponse("App View 2!")